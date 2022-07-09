

import nerdfonts as nf
from termcolor import colored


def format_text(value, text, length):

    if text == None:
        text = '{0:.2f}%'.format(value * 100)
    
    if text.startswith(' ') == False:
        text = ' ' + text

    return text.ljust(length,' ')


# def color(text='',barchar='',fg_color,bg_color):
#     pass    

def get_nth(this_list,index,default):
    try:
        return this_list[index]
    except IndexError:
        return default


def bar(
    start_full = '[',
    start_empty = '{',
    fill = '#',
    fill_end = '#',
    empty = ' ',
    end_full = ']',
    end_empty = '}',
    value = 0.6666,
    text = None,
    length = 50,
    color = 'green',
    empty_color = 'grey'
    ):

    on_color = 'on_' + empty_color

    value = min([max([0.0,value]),1.0])

    text = format_text(value=value, text=text,length=length)
    text = list(text)
        
    fill_count = int(value * length)
    mbar = ('+'*fill_count).ljust(length,'-')
    mbar = list(mbar)

    # print(len(mbar))

    result = ''
    for index,i in enumerate(mbar):
        if i == '+':
            if index == 0:
                result += colored(start_full,color=color)
            elif index == (length-1):
                result += colored(end_full,color=color)
            else:
                if get_nth(text,index,' ') == ' ':

                    if get_nth(mbar,index+1,'') == '-':
                        result += colored(fill_end,color=color,on_color=on_color)
                    else:
                        result += colored(fill,color=color,on_color=on_color)
                else:
                    result += colored(text[index],color='grey',on_color='on_'+color)
        else:
            if index == 0:
                result += colored(start_empty,color=empty_color)
            elif index == (length-1):
                result += colored(end_empty,color=empty_color)
            else:
                if get_nth(text,index,' ') == ' ':
                    result += colored(empty,on_color='on_'+empty_color)
                else:
                    result += colored(text[index],color='grey',on_color='on_'+empty_color)
        # print(i,' ',result)
    return result




def bubble_bar(value=0.75,length=50,text=None,color='green',on_color='red'):
    return bar(
        value=value,
        start_full=nf.icons['ple_left_half_circle_thick'],
        start_empty = nf.icons['ple_left_half_circle_thick'],
        fill = '\u2588',
        fill_end = nf.icons['ple_right_half_circle_thick'],
        empty = ' ',
        end_full = nf.icons['ple_right_half_circle_thick'],
        end_empty = nf.icons['ple_right_half_circle_thick'],
        text = text,
        length = length,
        color = color,
        empty_color = on_color
        )

def slant_bar(value=0.75,length=50,text=None,color='green',on_color='red'):
    return bar(
        value=value,
        start_full=nf.icons['ple_lower_right_triangle'],
        start_empty = nf.icons['ple_lower_right_triangle'],
        fill = '\u2588',
        fill_end = nf.icons['ple_upper_left_triangle'],
        empty = ' ',
        end_full = nf.icons['ple_upper_left_triangle'],
        end_empty = nf.icons['ple_upper_left_triangle'],
        text = text,
        length = length,
        color = color,
        empty_color = on_color
        )

def fire_bar(value=0.75,length=50,text=None,color='green',on_color='red'):
    return bar(
        value=value,
        start_full=nf.icons['ple_flame_thick_mirrored'],
        start_empty = nf.icons['ple_flame_thick_mirrored'],
        fill = '\u2588',
        fill_end = nf.icons['ple_flame_thick'],
        empty = ' ',
        end_full = nf.icons['ple_flame_thick'],
        end_empty = nf.icons['ple_flame_thick'],
        text = text,
        length = length,
        color = color,
        empty_color = on_color
        )

def data_bar(value=0.75,length=50,text=None,color='green',on_color='red'):
    return bar(
        value=value,
        start_full=nf.icons['ple_pixelated_squares_big_mirrored'],
        start_empty = nf.icons['ple_pixelated_squares_big_mirrored'],
        fill = '\u2588',
        fill_end = nf.icons['ple_pixelated_squares_small'],
        empty = ' ',
        end_full = nf.icons['ple_pixelated_squares_big'],
        end_empty = nf.icons['ple_pixelated_squares_big'],
        text = text,
        length = length,
        color = color,
        empty_color = on_color
        )

def diamond_bar(value=0.75,length=50,text=None,color='green',on_color='red'):
    return bar(
        value=value,
        start_full=nf.icons['pl_right_hard_divider'],
        start_empty = nf.icons['pl_right_hard_divider'],
        fill = '\u2588',
        fill_end = nf.icons['pl_left_hard_divider'],
        empty = ' ',
        end_full = nf.icons['pl_left_hard_divider'],
        end_empty = nf.icons['pl_left_hard_divider'],
        text = text,
        length = length,
        color = color,
        empty_color = on_color
        )

if __name__ == "__main__":
    import time
    
    # for k in nf.icons.keys():
    #     if k.startswith('pl'):
    #         print(k," : ", nf.icons[k])
    
    print(bubble_bar(value=0.0))
    print(bubble_bar(value=0.25))
    print(bubble_bar(value=0.5))
    print(bubble_bar(value=0.75))
    print(bubble_bar(value=1.0))


    for i in range(101):
        print(bubble_bar(value=(i/100.0),color='cyan',on_color='blue'),end='\r')
        # print(slant_bar(value=(i/100.0)),end='\r')
        # print(fire_bar(value=(i/100.0)),end='\r')
        # print(data_bar(value=(i/100.0)),end='\r')
        # print(diamond_bar(value=(i/100.0)),end='\r')

        # print(bubble_bar(value=(i/100.0),length=20,color='cyan',on_color='grey'),end='\r')

        time.sleep(0.01)
    bubble_bar(value=1.0)