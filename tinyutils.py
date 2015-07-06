import subprocess


def network():

    # Using subprocess.Popen() we can execute a Linux command from within
    # Python. The full command redirects the output in variable 'output' and
    # errors, if any, to 'err' variable

    output, err = \
        subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE).communicate()

    # 'output' variable has data in bytes. We want to have string. Using
    # decode() method we can convert it by specifying appropriate encoding

    output_list = output.decode("utf-8").split("\n")
    interfaces = []

    # The kind of output we are interested in is:
    #   1: lo: <LOOPB....
    #   2: eth0: <NO....
    # So if a line starts with a digit like 1, 2, 3, we split it. Else we
    # ignore it.

    for i in output_list:
        if i and i[0].isdigit():
            interfaces.append(i.split(': ')[1])

    # Finally we just return the interfaces

    return (interfaces)


def cpu():

    output, err = \
        subprocess.Popen(['lscpu'], stdout=subprocess.PIPE).communicate()

    # 'output' variable has data in bytes. We want to have string. Using
    # decode() method we can convert it by specifying appropriate encoding

    output = output.decode("utf-8").split("\n")
    output_list = []
    attributes = ['Model name', 'Architecture',
                  'Socket(s)', 'Core(s) per socket', 'Thread(s) per core', 'CPU(s)', 'Virtualization']

    # The kind of output we want are interested in is:
    # CPU Name: Intel Core i7 5970x @ 4.0 Ghz
    # Cores of the CPU : 8
    # Threads CPU can run : 16
    # More .......
    # All the needed CPU attributes are stored in the list attributes
    # Now we'll parse the attribute data from output and append it
    # to the output_list

    for attrib in attributes:
        for item in output:
            if item.split(":")[0] == attrib:
                output_list.append(item)

    return output_list


def memory():

    output, err = \
        subprocess.Popen(['cat','/proc''/meminfo'], stdout=subprocess.PIPE).communicate()

    # 'output' variable has data in bytes. We want to have string. Using
    # decode() method we can convert it by specifying appropriate encoding

    output = output.decode("utf-8").split("\n")
    mem_list=[]
    mem_attributes=['MemTotal', 'MemFree','Cached','Buffers','SwapCached','Active','Inactive','SwapTotal','SwapFree','PageTables' ]

    #The kind of output we are interested in is:
    #MemTotal:3913140 kB
    #MemFree:2212592 kB
    #Cached:1057776 kB
    #Buffers: 68596 kB
    #SwapCached:0 kB
    #and further details
    #After parsing the mem_attributes data from output,append it to mem_list
    #and than return mem_list
    
    for j in mem_attributes:
        for i in output:
            if i.split(":")[0] == j:
                mem_list.append(i)
    return mem_list


def main():
    # Calls all available modules
    print("\nmemory info\n",memory())
    print("\nnetwork interfaces\n",network())
    print("\ncpu info \n",cpu())


if __name__ == "__main__":
    # Do not forget this! Otherwise, nothing will seem to be working. :)

    main()
