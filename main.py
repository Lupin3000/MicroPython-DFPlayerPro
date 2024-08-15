from micropython import const
from lib.dfplayerpro import DFPlayerPro


UART_TX_GPIO = const(17)
UART_RX_GPIO = const(16)


if __name__ == '__main__':
    dfplayer = DFPlayerPro(tx_pin=UART_TX_GPIO, rx_pin=UART_RX_GPIO)

    response = dfplayer.test_connection()
    print(response)

    dfplayer.set_volume(15)
    dfplayer.set_play_mode(4)
    dfplayer.play_next()
