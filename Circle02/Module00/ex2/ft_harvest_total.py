#!/usr/bin/env python3

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tkorytko <tkorytko@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/17 14:29:25 by tkorytko            #+#    #+#            #
#   Updated: 2026/02/17 14:29:25 by tkorytko           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    d = int(input("Day 1 harvest: "))
    d += int(input("Day 2 harvest: "))
    d += int(input("Day 3 harvest: "))
    print("Total harvest: ", d)
