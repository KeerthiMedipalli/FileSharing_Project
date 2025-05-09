import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QTextEdit, QMessageBox
)
import encryptor
import blockchain

class FileSharingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔐 Secure Decentralized File Sharing")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Choose a file to encrypt and store")
        self.select_btn = QPushButton("📁 Select File")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout.addWidget(self.label)
        layout.addWidget(self.select_btn)
        layout.addWidget(self.output)

        self.setLayout(layout)
        self.select_btn.clicked.connect(self.select_file)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose a file to encrypt")
        if file_path:
            self.output.append(f"🔹 Selected File: {file_path}")
            try:
                bin_path, hash_value = encryptor.encrypt_file(file_path)
                record = blockchain.add_record(hash_value, owner="GUI_User")
                self.output.append(f"✅ File Encrypted and Saved: {bin_path}")
                self.output.append(f"🔗 Blockchain Record: {record}")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSharingApp()
    window.show()
    sys.exit(app.exec_())
