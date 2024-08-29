from micropython import const
from machine import Pin, UART
from time import sleep_ms


class DFPlayerPro:
    """
    MicroPython class for communication with the DFRobot DFPlayer Pro over UART.
    """

    DELAY_SEND_COMMAND = const(100)
    DELAY_TEST_CONNECTION = const(500)

    def __init__(self, tx_pin: int, rx_pin: int, baudrate: int = 115200, uart_id: int = 1):
        """
        Initialize the UART object.

        :param tx_pin: The GPIO number used for TX (transmit) communication.
        :type tx_pin: int
        :param rx_pin: The GPIO number used for RX (receive) communication.
        :type rx_pin: int
        :param baudrate: The desired baud rate for the UART communication (default: 115200).
        :type baudrate: int
        :param uart_id: The ID of the UART peripheral to use (default: 1).
        :type uart_id: int
        """
        uart = int(uart_id)
        baud = int(baudrate)
        tx = int(tx_pin)
        rx = int(rx_pin)

        self.uart = UART(uart, baudrate=baud, tx=Pin(tx), rx=Pin(rx))
        self.uart.init(baudrate=baudrate, bits=8, parity=None, stop=1)

    def _send_command(self, command: str) -> str:
        """
        Sends a command to a device and returns the response.

        :param command: The command to send.
        :type command: str
        :return: The response received from the device.
        :rtype: str
        """
        full_command = f"AT+{command}\r\n"

        print(f"[INFO] request: {full_command}")
        self.uart.write(full_command)
        sleep_ms(self.DELAY_SEND_COMMAND)

        response = self.uart.read()
        print(f"[INFO] response: {response}")
        return response.decode('utf-8') if response else None

    def test_connection(self):
        """
        Test the connection by sending an AT command via UART.

        :return: The response received from the device as a decoded string, or None if no response was received.
        """
        self.uart.write("AT\r\n")
        sleep_ms(self.DELAY_TEST_CONNECTION)

        response = self.uart.read()
        print(f"[INFO] response: {response}")
        return response.decode('utf-8') if response else None

    def set_volume(self, volume: int) -> str:
        """
        Set the volume of the device.

        :param volume: The volume level to set.
        :return: The response from sending the volume command.
        :rtype: str
        :raises ValueError: If the volume is not between 0 and 30.
        """
        if volume < 0 or volume > 30:
            raise ValueError("[ERROR] Volume must be between 0 and 30")

        return self._send_command(f"VOL={volume}")

    def set_play_mode(self, mode: int) -> str:
        """
        Set the play mode of the media player.
            1: repeat one song
            2: repeat all
            3: play one song and pause
            4: Play randomly
            5: Repeat all in the folder

        :param mode: The play mode to set. Valid values are: 1, 2, 3, 4, and 5.
        :return: The response message from the media player.
        :rtype: str
        :raises: ValueError: If the provided play mode is invalid.
        """
        if int(mode) not in [1, 2, 3, 4, 5]:
            raise ValueError("[ERROR] Invalid play mode")

        return self._send_command(f"PLAYMODE={mode}")

    def set_baudrate(self, baudrate: int) -> str:
        """
        Set UART baudrate

        :param baudrate: The baud rate to be set. Valid values are: 9600, 19200, 38400, 57600, 115200.
        :return: A string indicating the success of the operation.
        :raises ValueError: If the provided baud rate is invalid.
        """
        if int(baudrate) not in [9600, 19200, 38400, 57600, 115200]:
            raise ValueError("[ERROR] Invalid baudrate")

        return self._send_command(f"BAUDRATE={baudrate}")

    def query_volume(self) -> str:
        """
        Query the volume level in the device.

        :return: The volume level as a string.
        :rtype: str
        """
        return self._send_command("VOL=?")

    def query_play_mode(self) -> str:
        """
        Query the play mode of the device.

        :return: The current play mode of the device.
        :rtype: str
        """
        return self._send_command("PLAYMODE=?")

    def query_playing_file_number(self) -> str:
        """
        Query the playing file number.

        :return: The playing file number.
        :rtype: str
        """
        return self._send_command("QUERY=1")

    def query_total_file_count(self) -> str:
        """
        Query the total file count.

        :return: The total file count as a string.
        :rtype: str
        """
        return self._send_command("QUERY=2")

    def query_played_time(self) -> str:
        """
        Query the played time.

        :return: The played time as a string.
        :rtype: str
        """
        return self._send_command("QUERY=3")

    def query_total_time(self) -> str:
        """
        Queries and returns the total time.

        :return: The total time as a string.
        :rtype: str
        """
        return self._send_command("QUERY=4")

    def query_playing_file_name(self) -> str:
        """
        Returns the name of the currently playing file.

        :return: The name of the currently playing file as a string.
        :rtype: str
        """
        return self._send_command("QUERY=5")

    def amplifier_on(self) -> str:
        """
        Turns on the amplifier.

        :return: The response from sending the "AMP=ON" command.
        :rtype: str
        """
        return self._send_command("AMP=ON")

    def amplifier_off(self) -> str:
        """
        Turns off the amplifier.

        :return: The response from sending the "AMP=OFF" command.
        :rtype: str
        """
        return self._send_command("AMP=OFF")

    def prompt_on(self) -> str:
        """
        Enable prompt on the device.

        :return: The response from sending the command "PROMPT=ON".
        :rtype: str
        """
        return self._send_command("PROMPT=ON")

    def prompt_off(self) -> str:
        """
        Turn off the prompt functionality.

        :return: The response from executing the command "PROMPT=OFF".
        :rtype: str
        """
        return self._send_command("PROMPT=OFF")

    def led_on(self) -> str:
        """
        Turns on the LED.

        :return: The response from executing the command "LED=ON".
        :rtype: str
        """
        return self._send_command("LED=ON")

    def led_off(self) -> str:
        """
        Turns off the LED.

        :return: The response from executing the command "LED=OFF".
        :rtype: str
        """
        return self._send_command("LED=OFF")

    def play_next(self) -> str:
        """
        Plays the next track in the playlist.

        :return: The response from the "PLAY=NEXT" command.
        :rtype: str
        """
        return self._send_command("PLAY=NEXT")

    def play_last(self) -> str:
        """
        Plays the previous track in the playlist.

        :return: The response from the "PLAY=LAST" command.
        :rtype: str
        """
        return self._send_command("PLAY=LAST")

    def play_pause(self) -> str:
        """
        Play or pause the playback.

        :return: The result of the "PLAY=PP" command.
        :rtype: str
        """
        return self._send_command("PLAY=PP")

    def fast_rewind(self, seconds: int) -> str:
        """
        Fast Rewind the playback by a specified number of seconds.

        :param seconds: The number of seconds to rewind the media.
        :type seconds: int
        :return: The result of the "TIME=-{seconds}" command.
        :rtype: str
        """
        sec = int(seconds)

        return self._send_command(f"TIME=-{sec}")

    def fast_forward(self, seconds: int) -> str:
        """
        Fast forwards the playback by the specified number of seconds.

        :param seconds: The number of seconds to forward the media.
        :type seconds: int
        :return: The result of the "TIME=+{seconds}" command.
        :rtype: str
        """
        sec = int(seconds)

        return self._send_command(f"TIME=+{sec}")

    def start_from_second(self, second: int) -> str:
        """
        Starts the playback by a specified number of seconds.

        :param second: The second to start from as an integer.
        :type second: int
        :return: The result of the "TIME={second}" command.
        :rtype: str
        """
        sec = int(second)

        return self._send_command(f"TIME={sec}")

    def play_file_by_number(self, number: int) -> str:
        """
        Play a file by its number.

        :param number: The number of the file to be played.
        :type number: int
        :return: The result of the "PLAYNUM={number}" command.
        :rtype: str
        """
        num = int(number)

        return self._send_command(f"PLAYNUM={num}")

    def play_file_by_path(self, path: str) -> str:
        """
        Plays a file by the given file path.

        :param path: The file path of the file to play.
        :type path: str
        :return: The result of the "PLAYFILE={path}" command.
        :rtype: str
        """
        file_path = str(path)

        return self._send_command(f"PLAYFILE={file_path}")

    def delete_playing_file(self) -> str:
        """
        Delete the playing file.

        :return: The response from sending the "DEL" command.
        :rtype: str
        """
        return self._send_command("DEL")

    def record_and_pause(self) -> str:
        """
        Records audio and pauses the recording.

        :return: The response from sending the "REC=RP" command.
        :rtype: str
        """
        return self._send_command("REC=RP")

    def save_recording(self) -> str:
        """
        Saves the recording.

        :return: The response from the "REC=SAVE" method.
        :rtype: str
        """
        return self._send_command("REC=SAVE")
