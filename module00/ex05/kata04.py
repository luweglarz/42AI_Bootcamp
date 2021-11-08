t = ( 0, 4, 132.42222, 10000, 12345.67)
print("module_{0:0>2}".format(t[0]), "ex_{0:0>2}".format(t[1]), ": ", end='')
print("{:.2f}".format(t[2]), "{:.2e}".format(t[3]), "{:.2e}".format(t[4]))