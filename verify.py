#!/usr/bin/python  
import argparse
import yaml
from yaml.loader import SafeLoader


class DNSValidator:
    dns_records = None
    config_path = None

    def __init__(self, config_path: str = "expected.yaml"):
        self.config_path = config_path

    def load_dns_record(self):
        with open(self.config_path) as f:
            self.dns_records = yaml.load(f, Loader=SafeLoader)
        print(self.dns_records)


if __name__ == '__main__':

    """python argument parser used for receiving and parsing arguments passed form the command line console whe 
    running the script """
    parser = argparse.ArgumentParser()

    parser.add_argument('config', type=str)  # argument config file name holder
    parser.add_argument('domain', type=str)  # argument domain name holder
    parser.add_argument('nameserver', type=str)  # argument domain nameserver string holder

    args = parser.parse_args()  # parse the supplied arguments from the

    config = args.config  # configuration file yaml file name
    domain = args.domain  # domain group equivalent to the domain group name e.g. foo.bar
    nameserver = args.nameserver  # domain server name

    # print(config)

    dns_validator = DNSValidator(config)
    dns_validator.load_dns_record()
    print(dns_validator.dns_records)

    # dns_records = dns_validator.dns_records
    """
    match if domain name server matches
    """
    if nameserver ==  dns_validator.dns_records[domain]["value"]:
        print(f"""[OK] {nameserver} records matches  """)
