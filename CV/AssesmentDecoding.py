from qrtools import QR
import os


def find_qr_code(img_file):
    """

    :param img_file:
    :return:
    """
    print(img_file)
    myCode = QR(filename=img_file)
    if myCode.decode():
        print myCode.data
        print myCode.data_type
        print myCode.data_to_string()

if __name__ == '__main__':
    find_qr_code(os.path.join(os.path.dirname(__file__),"sample.png"))