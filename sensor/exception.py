import os
import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in script: {filename} "
        f"at line number: {line_number} "
        f"error message: {str(error)}"
    )
    return error_message


class sensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

       
        error_message_detail_str = error_message_detail(
            error_message, error_detail=error_detail
        )
        self.error_message = error_message_detail_str

    def __str__(self):
        return self.error_message
