from fins import FinsConnection
import usb


def assemble_data_packet(command):
    """Assemble USB data packet
        type command: bytes
    """
    length = len(command) + 2
    data_packet = 0xab + length.to_bytes(2, 'big') + command
    check_sum = 0
    for b in data_packet:
        check_sum += b
    data_packet += check_sum.to_bytes(2, 'big')
    return data_packet


class USBFinsConnection(FinsConnection):

    def __init__(self):
        FinsConnection.__init__(self)

    def execute_fins_command_frame(self, fins_command_frame):
        """Sends FINS command using this connection

        Implements the abstract method required of FinsConnection
        :param fins_command_frame:
        :return: :raise:
        """
        # Create a USB device with omron vendor ID and sysmac PLC product ID
        dev = usb.core.find(idVendor=0x0590, idProduct=0x005b)
        """:type : fins.core.Device """
        if dev is None:
            raise ValueError('Device not found')
        else:
            # dev.set_configuration()
            data_packet = assemble_data_packet(fins_command_frame)
            dev.write(1, data_packet)
            # Read response from USB 130 endpoint
            response_array = dev.read(130, 1024)
            # USB creates garbage malformed packet after real response that we need to clear
            trash = dev.read(130, 1024)
        check_sum = 0
        for element in response_array[0:-2]:
            check_sum += element
        if check_sum == int.from_bytes(response_array[-2:], 'big'):
            response = response_array[3:-2]
        else:
            response = None
        return response
