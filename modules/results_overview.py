import os
import subprocess
import platform
import zipfile2
import xml.etree.ElementTree as ET
import json
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . settings import Settings


class ResultsOverview:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.settings = Settings()
        self.selected_file_path = None

        self.setup_ui()

    def setup_ui(self):
        # Use the UI-defined widgets instead of creating them programmatically
        self.folder_tree = self.widgets.fileTreeWidget
        self.content_stack = self.widgets.fileContentStack
        self.data_table = self.widgets.fileContentTable
        self.web_browser = self.widgets.webContentBrowser
        self.text_editor = self.widgets.textContentEditor
        self.image_preview = self.widgets.imagePreviewLabel
        self.image_scroll_area = self.widgets.imageScrollArea
        self.status_label = self.widgets.fileStatusLabel
        self.open_file_button = self.widgets.openFileButton
        self.open_directory_button = self.widgets.openDirectoryButton

        # Connect signals
        self.folder_tree.itemClicked.connect(self.on_file_selected)
        self.open_file_button.clicked.connect(self.open_selected_file)
        self.open_directory_button.clicked.connect(self.open_run_directory)

        # Configure table widget
        self.data_table.horizontalHeader().setStretchLastSection(True)

        # Initially disable the open file button
        self.open_file_button.setEnabled(False)

        # Set splitter proportions (30% left, 70% right)
        self.widgets.resultsSplitter.setSizes([300, 700])

        # Set default stack page to table view
        self.content_stack.setCurrentIndex(0)

    def load_run_data(self):
        """Load data when a run is selected"""
        if not Settings.SELECTED_RUN:
            self.status_label.setText("Select a file to view its contents")
            self.folder_tree.clear()
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            return

        run_path = os.path.join(Settings.RUNS_DIR, Settings.SELECTED_RUN)

        # Load folder structure
        self.load_folder_structure(run_path)

        # Load Excel data (first peak file)
        self.load_peak_data(run_path)

    def load_folder_structure(self, run_path):
        """Populate the folder tree with run directory contents"""
        self.folder_tree.clear()

        if not os.path.exists(run_path):
            return

        # Create root item
        root_item = QTreeWidgetItem([Settings.SELECTED_RUN])
        root_item.setData(0, Qt.UserRole, run_path)
        self.folder_tree.addTopLevelItem(root_item)

        # Recursively add items
        self.add_folder_items(root_item, run_path)

        # Expand root
        root_item.setExpanded(True)

    def add_folder_items(self, parent_item, folder_path):
        """Recursively add folder contents to tree"""
        try:
            items = os.listdir(folder_path)
            items.sort()  # Sort alphabetically

            for item_name in items:
                item_path = os.path.join(folder_path, item_name)
                tree_item = QTreeWidgetItem([item_name])
                tree_item.setData(0, Qt.UserRole, item_path)

                if os.path.isdir(item_path):
                    # Folder
                    tree_item.setIcon(0, self.main_window.style().standardIcon(QStyle.SP_DirIcon))
                    self.add_folder_items(tree_item, item_path)
                else:
                    # File
                    tree_item.setIcon(0, self.main_window.style().standardIcon(QStyle.SP_FileIcon))

                parent_item.addChild(tree_item)

        except PermissionError:
            pass  # Skip folders we can't read

    def load_peak_data(self, run_path):
        """Load the first peak Excel file data"""
        bed2peak_path = os.path.join(run_path, "bed2peak")

        if not os.path.exists(bed2peak_path):
            self.status_label.setText("No bed2peak directory found")
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            self.content_stack.setCurrentIndex(0)
            return

        # Look for the peak Excel file first, then fall back to txt file
        peak_excel_file = os.path.join(bed2peak_path, "aligned.d0.peak.merge.xlsx")
        peak_txt_file = os.path.join(bed2peak_path, "aligned.d0.peak.merge.txt")

        if os.path.exists(peak_excel_file):
            peak_file = peak_excel_file
        elif os.path.exists(peak_txt_file):
            peak_file = peak_txt_file
        else:
            self.status_label.setText("No aligned.d0.peak.merge file found (.xlsx or .txt)")
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            self.content_stack.setCurrentIndex(0)
            return

        try:
            if peak_file.endswith('.xlsx'):
                data, headers = self.read_xlsx_file(peak_file)
            else:
                data, headers = self.read_txt_file(peak_file)

            # Set up table
            self.data_table.setRowCount(len(data))
            self.data_table.setColumnCount(len(headers))
            self.data_table.setHorizontalHeaderLabels(headers)

            # Populate table
            for row_idx, row_data in enumerate(data):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.data_table.setItem(row_idx, col_idx, item)

            # Resize columns to content
            self.data_table.resizeColumnsToContents()

            file_name = os.path.basename(peak_file)
            self.status_label.setText(f"Loaded {len(data)} peaks from {file_name}")

        except Exception as e:
            self.status_label.setText(f"Error loading text file: {str(e)}")
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            self.content_stack.setCurrentIndex(0)

    def on_file_selected(self, item, column):
        """Handle file selection in tree"""
        file_path = item.data(0, Qt.UserRole)
        self.selected_file_path = file_path

        # Enable button only for files
        if os.path.isfile(file_path):
            self.open_file_button.setEnabled(True)
            self.load_file_content(file_path)
        else:
            self.open_file_button.setEnabled(False)
            file_name = os.path.basename(file_path)
            self.status_label.setText(f"Selected: {file_name}")
            # Switch to table view and clear it
            self.content_stack.setCurrentIndex(0)
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)

    def load_file_content(self, file_path):
        """Load and display file content based on file type"""
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_path)[1].lower()

        try:
            if file_ext in ['.txt', '.xlsx']:
                # Show tabular data
                self.content_stack.setCurrentIndex(0)
                self.load_tabular_file(file_path)
            elif file_ext in ['.html', '.htm']:
                # Show HTML content
                self.content_stack.setCurrentIndex(1)
                self.load_html_file(file_path)
            elif file_ext == '.pdf':
                # Show PDF preview as image
                self.content_stack.setCurrentIndex(3)
                self.load_pdf_file(file_path)
            elif file_ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif', '.ico']:
                # Show image files
                self.content_stack.setCurrentIndex(3)
                self.load_image_file(file_path)
            elif file_ext == '.json':
                # Show JSON content with formatting
                self.content_stack.setCurrentIndex(2)
                self.load_json_file(file_path)
            elif file_ext in ['.zip', '.tar', '.gz', '.rar', '.7z']:
                # Show message for compressed files
                self.content_stack.setCurrentIndex(1)
                self.show_unsupported_file_message(file_path, "compressed archive")
            elif file_ext in ['.exe', '.bin', '.dll', '.so']:
                # Show message for binary files
                self.content_stack.setCurrentIndex(1)
                self.show_unsupported_file_message(file_path, "binary")
            elif file_ext == '.svg':
                # Show message for SVG files (require special handling)
                self.content_stack.setCurrentIndex(1)
                self.show_unsupported_file_message(file_path, "SVG image")
            else:
                # Try to show as plain text
                self.content_stack.setCurrentIndex(2)
                self.load_text_file(file_path)
        except Exception as e:
            self.status_label.setText(f"Error loading {file_name}: {str(e)}")
            # Switch to table view and clear it
            self.content_stack.setCurrentIndex(0)
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)

    def load_tabular_file(self, file_path):
        """Load txt or xlsx files into table view"""
        try:
            if file_path.endswith('.xlsx'):
                data, headers = self.read_xlsx_file(file_path)
            else:
                data, headers = self.read_txt_file(file_path)

            # Set up table
            self.data_table.setRowCount(len(data))
            self.data_table.setColumnCount(len(headers))
            self.data_table.setHorizontalHeaderLabels(headers)

            # Populate table
            for row_idx, row_data in enumerate(data):
                for col_idx, value in enumerate(row_data):
                    item_widget = QTableWidgetItem(str(value))
                    self.data_table.setItem(row_idx, col_idx, item_widget)

            # Resize columns to content
            self.data_table.resizeColumnsToContents()

            file_name = os.path.basename(file_path)
            self.status_label.setText(f"Loaded {len(data)} rows from {file_name}")

        except Exception as e:
            raise Exception(f"Error loading tabular file: {str(e)}")

    def load_html_file(self, file_path):
        """Load HTML file into web browser"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Set HTML content to the browser
            self.web_browser.setHtml(content)

            file_name = os.path.basename(file_path)
            self.status_label.setText(f"Displaying HTML: {file_name}")

        except Exception as e:
            raise Exception(f"Error loading HTML file: {str(e)}")

    def load_pdf_file(self, file_path):
        """Load PDF file and show all pages as image previews"""
        try:
            file_name = os.path.basename(file_path)

            # Try to convert PDF pages to images
            try:
                import fitz  # PyMuPDF

                # Open PDF document
                doc = fitz.open(file_path)
                if len(doc) > 0:
                    page_count = len(doc)
                    self.display_pdf_pages(doc, file_name)
                    doc.close()
                    self.status_label.setText(f"PDF preview: {file_name} ({page_count} pages) - Click 'Open in Default App' for full view")
                    return
                else:
                    doc.close()
                    raise Exception("PDF has no pages")

            except ImportError:
                # PyMuPDF not available, fall back to message
                pass
            except Exception as pdf_error:
                print(f"PDF preview error: {pdf_error}")

            # Fallback: show message that PDF preview is not available
            self.show_pdf_fallback_message(file_name, file_path)

        except Exception as e:
            raise Exception(f"Error loading PDF file: {str(e)}")

    def display_pdf_pages(self, doc, file_name):
        """Display all PDF pages in a scrollable layout"""
        import fitz  # Import here since it's needed in this method

        # Clear the current scroll area content
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(10)
        scroll_layout.setContentsMargins(10, 10, 10, 10)

        max_width = 600  # Reasonable width for PDF pages

        # Process each page
        for page_num in range(len(doc)):
            try:
                page = doc[page_num]
                # Render page to pixmap with good quality
                mat = fitz.Matrix(1.5, 1.5)  # 1.5x zoom for good quality but manageable size
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("png")

                # Create QPixmap from the image data
                pixmap = QPixmap()
                if pixmap.loadFromData(img_data):
                    # Scale to reasonable width while maintaining aspect ratio
                    if pixmap.width() > max_width:
                        scaled_pixmap = pixmap.scaledToWidth(max_width, Qt.TransformationMode.SmoothTransformation)
                    else:
                        scaled_pixmap = pixmap

                    # Create label for this page
                    page_label = QLabel()
                    page_label.setPixmap(scaled_pixmap)
                    page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    page_label.setStyleSheet("QLabel { border: 1px solid #ccc; background: white; margin: 5px; }")

                    # Add page number label
                    page_number_label = QLabel(f"Page {page_num + 1}")
                    page_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    page_number_label.setStyleSheet("QLabel { font-weight: bold; color: #666; margin: 2px; }")

                    scroll_layout.addWidget(page_number_label)
                    scroll_layout.addWidget(page_label)

            except Exception as e:
                # If a page fails, add an error message
                error_label = QLabel(f"Error loading page {page_num + 1}: {str(e)}")
                error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                error_label.setStyleSheet("QLabel { color: red; margin: 5px; }")
                scroll_layout.addWidget(error_label)

        # Add stretch at the end
        scroll_layout.addStretch()

        # Set the widget to the scroll area
        self.image_scroll_area.setWidget(scroll_widget)

    def show_pdf_fallback_message(self, file_name, file_path):
        """Show fallback message when PDF preview is not available"""
        # Switch to web browser view for the message
        self.content_stack.setCurrentIndex(1)

        html_content = f"""
        <html>
        <head><title>PDF Viewer</title></head>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>PDF File: {file_name}</h2>
            <p><strong>Note:</strong> PDF preview is not available.</p>
            <p>To view the PDF, click the "Open in Default App" button to open it in your default PDF viewer.</p>
            <p><strong>File Location:</strong> {file_path}</p>
            <hr>
            <p style="color: #666; font-style: italic;">
                PDF preview requires PyMuPDF library. Install with: pip install PyMuPDF
            </p>
        </body>
        </html>
        """

        self.web_browser.setHtml(html_content)
        self.status_label.setText(f"PDF file selected: {file_name} - Click 'Open in Default App' to view")

    def load_image_file(self, file_path):
        """Load and display image files"""
        try:
            file_name = os.path.basename(file_path)

            # Load image using QPixmap
            pixmap = QPixmap(file_path)

            if pixmap.isNull():
                raise Exception("Could not load image file")

            self.display_image(pixmap, f"Image: {file_name}")
            self.status_label.setText(f"Displaying image: {file_name}")

        except Exception as e:
            raise Exception(f"Error loading image file: {str(e)}")

    def display_image(self, pixmap, title):
        """Display a QPixmap in the image preview widget"""
        # Create a new widget for the scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(10, 10, 10, 10)
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Calculate appropriate size for display
        max_width = 800
        max_height = 600

        # Scale image if it's too large, maintaining aspect ratio
        if pixmap.width() > max_width or pixmap.height() > max_height:
            scaled_pixmap = pixmap.scaled(max_width, max_height,
                                        Qt.AspectRatioMode.KeepAspectRatio,
                                        Qt.TransformationMode.SmoothTransformation)
        else:
            scaled_pixmap = pixmap

        # Create a label for the image
        image_label = QLabel()
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        scroll_layout.addWidget(image_label)

        # Set the widget to the scroll area
        self.image_scroll_area.setWidget(scroll_widget)

    def show_unsupported_file_message(self, file_path, file_type):
        """Show message for unsupported file types"""
        file_name = os.path.basename(file_path)

        # Show a nice HTML message about unsupported file types
        html_content = f"""
        <html>
        <head><title>Unsupported File</title></head>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>File: {file_name}</h2>
            <p><strong>Note:</strong> This {file_type} file cannot be displayed in the preview.</p>
            <p>To view the file, click the "Open in Default App" button to open it with your system's default application.</p>
            <p><strong>File Location:</strong> {file_path}</p>
            <hr>
            <p style="color: #666; font-style: italic;">
                Some file types require specialized applications to view their content properly.
            </p>
        </body>
        </html>
        """

        # Switch to web browser view to show the HTML content
        self.content_stack.setCurrentIndex(1)
        self.web_browser.setHtml(html_content)
        self.status_label.setText(f"Cannot preview {file_type} file: {file_name} - Click 'Open in Default App' to view")

    def load_json_file(self, file_path):
        """Load and format JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            # Pretty print the JSON
            formatted_json = json.dumps(json_data, indent=2, ensure_ascii=False)
            self.text_editor.setPlainText(formatted_json)

            file_name = os.path.basename(file_path)
            self.status_label.setText(f"Displaying JSON: {file_name}")

        except Exception as e:
            raise Exception(f"Error loading JSON file: {str(e)}")

    def load_text_file(self, file_path):
        """Load plain text file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.text_editor.setPlainText(content)

            file_name = os.path.basename(file_path)
            self.status_label.setText(f"Displaying text file: {file_name}")

        except Exception as e:
            # Try with different encoding
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
                self.text_editor.setPlainText(content)

                file_name = os.path.basename(file_path)
                self.status_label.setText(f"Displaying text file: {file_name} (latin-1 encoding)")
            except Exception:
                raise Exception(f"Error loading text file: {str(e)}")

    def read_txt_file(self, file_path):
        """Read tab-delimited text file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            return [], []

        # Check if first line looks like data (all numeric/genomic coordinates)
        first_line = lines[0].strip().split('\t')

        # For peak files, create appropriate headers
        if file_path.endswith('peak.merge.txt'):
            headers = ['Chromosome', 'Start', 'End', 'Name', 'Score', 'Strand', 'Peak_Height']
        else:
            # Try to determine if first line is headers or data
            if any(not col.replace('.', '').replace('-', '').isdigit() for col in first_line if col):
                # First line appears to be headers
                headers = first_line
                data_lines = lines[1:]
            else:
                # First line appears to be data, create generic headers
                headers = [f'Column_{i+1}' for i in range(len(first_line))]
                data_lines = lines

        # For peak files, all lines are data
        if file_path.endswith('peak.merge.txt'):
            data_lines = lines

        # Parse data lines
        data = []
        for line in data_lines:
            row = line.strip().split('\t')
            # Pad with empty strings if row is shorter than headers
            while len(row) < len(headers):
                row.append('')
            data.append(row)

        return data, headers

    def open_selected_file(self):
        """Open the selected file in the default application"""
        if not self.selected_file_path or not os.path.isfile(self.selected_file_path):
            return

        try:
            system = platform.system()
            if system == "Windows":
                os.startfile(self.selected_file_path)
            elif system == "Darwin":  # macOS
                subprocess.Popen(["open", self.selected_file_path])
            else:  # Linux and other Unix-like systems
                subprocess.Popen(["xdg-open", self.selected_file_path])
        except Exception as e:
            # Show error message if opening fails
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "Error",
                f"Could not open file: {str(e)}"
            )

    def open_run_directory(self):
        """Open the run directory in file explorer"""
        if not Settings.SELECTED_RUN:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "No Run Selected",
                "Please select a run first."
            )
            return

        filepath = os.path.join(Settings.RUNS_DIR, Settings.SELECTED_RUN)

        if not os.path.exists(filepath):
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "Directory Not Found",
                f"Run directory '{filepath}' does not exist."
            )
            return

        try:
            system = platform.system()
            if system == "Darwin":  # macOS
                subprocess.Popen(['open', filepath])
            elif system == "Windows":  # Windows
                os.startfile(filepath)
            else:  # Linux and other Unix-like systems
                subprocess.Popen(['xdg-open', filepath])
        except Exception as e:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "Error",
                f"Could not open directory: {str(e)}"
            )

    def read_xlsx_file(self, file_path):
        """Read Excel (.xlsx) file using built-in libraries"""
        try:
            with zipfile2.ZipFile(file_path, 'r') as zip_file:
                # Read shared strings
                shared_strings = []
                try:
                    shared_strings_xml = zip_file.read('xl/sharedStrings.xml')
                    shared_strings_root = ET.fromstring(shared_strings_xml)
                    for si in shared_strings_root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                        t_elem = si.find('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                        if t_elem is not None:
                            shared_strings.append(t_elem.text or '')
                        else:
                            shared_strings.append('')
                except KeyError:
                    # No shared strings file
                    pass

                # Read the first worksheet
                sheet_xml = zip_file.read('xl/worksheets/sheet1.xml')
                sheet_root = ET.fromstring(sheet_xml)

                # Parse rows and cells
                rows = []
                for row_elem in sheet_root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                    row_data = []
                    cells = row_elem.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')

                    # Sort cells by their reference (A1, B1, C1, etc.)
                    cells.sort(key=lambda c: self._excel_col_to_num(c.get('r', 'A1')))

                    current_col = 0
                    for cell in cells:
                        cell_ref = cell.get('r', 'A1')
                        col_num = self._excel_col_to_num(cell_ref)

                        # Fill in missing columns with empty strings
                        while current_col < col_num:
                            row_data.append('')
                            current_col += 1

                        cell_type = cell.get('t', '')
                        value_elem = cell.find('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')

                        if value_elem is not None:
                            value = value_elem.text or ''
                            if cell_type == 's':  # Shared string
                                try:
                                    value = shared_strings[int(value)]
                                except (IndexError, ValueError):
                                    pass
                        else:
                            value = ''

                        row_data.append(value)
                        current_col += 1

                    if row_data:  # Only add non-empty rows
                        rows.append(row_data)

                if not rows:
                    return [], []

                # Use first row as headers if it contains non-numeric data
                first_row = rows[0]
                if any(not str(cell).replace('.', '').replace('-', '').isdigit() for cell in first_row if cell):
                    headers = [str(cell) for cell in first_row]
                    data = rows[1:]
                else:
                    # Create generic headers
                    max_cols = max(len(row) for row in rows) if rows else 0
                    headers = [f'Column_{i+1}' for i in range(max_cols)]
                    data = rows

                # Ensure all rows have the same number of columns
                for row in data:
                    while len(row) < len(headers):
                        row.append('')

                return data, headers

        except Exception as e:
            raise Exception(f"Error reading Excel file: {str(e)}")

    def _excel_col_to_num(self, cell_ref):
        """Convert Excel cell reference (like 'B1') to column number (0-based)"""
        col_str = ''
        for char in cell_ref:
            if char.isalpha():
                col_str += char
            else:
                break

        result = 0
        for char in col_str:
            result = result * 26 + (ord(char.upper()) - ord('A') + 1)
        return result - 1
