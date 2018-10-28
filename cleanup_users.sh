#!/bin/bash

grep null /etc/passwd | cut -f1 -d':' | xargs -i sudo userdel {}

