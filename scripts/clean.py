#!/usr/bin/env python3

import click
import os
import shutil


@click.command()
def main():
    """Clean a PolyCode services."""
    
    for path in ('db-data', 'letsencrypt', 'proxy-data', '.env'):
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)


if __name__ == '__main__':
    main()
