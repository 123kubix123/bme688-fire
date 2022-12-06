from bme68x import BME68X
import json

def read_conf(path: str):
    with open(path, 'rb') as conf_file:
        conf = [int.from_bytes(bytes([b]), 'little') for b in conf_file.read()]
        conf = conf[4:]
    return conf

def main():
    s = BME68X(0x76, 0)
    BSEC_SAMPLE_RATE_HIGH_PERFORMANCE = 0.055556
    BSEC_SAMPLE_RATE_LP = 0.33333
    print(f'SUBSCRIBE GAS ESTIMATES {s.subscribe_gas_estimates(3)}')
    print(f'INIT BME68X {s.init_bme68x()}')
    print('\n\nSTARTING MEASUREMENT\n')
    while(True):
        print(s.get_bsec_data())
        try:
            data = s.get_digital_nose_data()
        except Exception as e:
            print(e)
            main()
        if data:
            print(data)           # entry = data[-1]

if __name__ == '__main__':
    main()
