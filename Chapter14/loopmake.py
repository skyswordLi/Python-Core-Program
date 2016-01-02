dashes = '\n' + '-' * 50
exec_dict = {

    'f': """
for %s in %s:
    print %s
""",

    's': """
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s += 1
""",

    'n': """
%s = %d
while %s < %d:
    print %s
    %s += %d
"""
}


def main():
    loop_type = raw_input('Loop type? (For/While) ')
    data_type = raw_input('Data type? (Number/Seq) ')

    if 'n' == data_type:
        start = input('Starting value? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Stepping value? ')
        seq = str(range(start, stop, step))
    else:
        seq = raw_input('Enter sequence: ')

    var = raw_input('Iterative variable name? ')

    if 'f' == loop_type:
        exec_str = exec_dict['f'] % (var, seq, var)
    elif 'w' == loop_type:
        if 's' == data_type:
            seq_var = raw_input('Enter sequence name? ')
            exec_str = exec_dict['s'] % (var, seq_var, seq, var, seq_var, seq_var, var, var)
        elif 'n' == data_type:
            exec_str = exec_dict['n'] % (var, start, var, stop, var, var, step)

    print dashes
    print 'Your custom-generated code:' + dashes
    print exec_str + dashes
    print 'Test execution of the code:' + dashes
    exec exec_str
    print dashes


if '__main__' == __name__:
    main()
