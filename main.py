from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from getpass import getpass
from zxcvbn import zxcvbn
from os import path

class PDF:

    @staticmethod
    def lock_file(filename: str, password: str) -> None:
        try:
            pdf_writer: PdfWriter = PdfWriter()

            with open(file=filename, mode="rb") as in_pdf:
                pdf_reader: PdfReader = PdfReader(in_pdf)

                for i, page_no in enumerate(range(len(pdf_reader.pages))):
                    pdf_writer.add_page(pdf_reader.pages[page_no])
                    # print(
                    #     "\rLocking page: {}/{}".format(i + 1, len(pdf_reader.pages)),
                    #     end="",
                    # )

                pdf_writer.encrypt(password)

            new_filename: str = "{}_locked.pdf".format(filename[:-4])

            with open(file=new_filename, mode="wb") as out_pdf:
                pdf_writer.write(out_pdf)

        except Exception as error:
            print(f"\nError: {str(error)}")

        else:
            print("\n[+] PDF Locked Successfully.")

    @staticmethod
    def get_password() -> str | None:
        try:
            while True:
                password: str = getpass("Enter the Password: ")

                result = zxcvbn(password=password)
                score: int = result.get("score", 0)
                response: str = ""

                if score >= 3:
                    return password

                feedback: dict = result.get("feedback", {})
                warning: str = feedback.get("warning", "")
                suggestions: list = feedback.get("suggestions", [])

                response += "\nWeak Password!"
                response += "\nWarning: {}".format(warning)
                response += "\nSuggestions: {}\n".format(", ".join(suggestions))

                print(response)

        except KeyboardInterrupt:
            return None

        except Exception as error:
            print(f"Error: {str(error)}")
            return None

    @staticmethod
    def main() -> None:
        try:
            filename: str = input("Enter the PDF name: ")

            if not path.exists(filename):
                print("\nFile not Found.")
                return

            password: str = PDF.get_password()

            if not password:
                return

            PDF.lock_file(filename=filename, password=password)

        except Exception as error:
            print(f"Error: {str(error)}")


if __name__ == "__main__":
    PDF.main()
