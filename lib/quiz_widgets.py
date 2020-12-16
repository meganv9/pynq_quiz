import random
import subprocess

from IPython.display import display, Markdown
from ipywidgets import *

try:
    from rich import print
except:
    subprocess.call(['pip', 'install', 'rich'])
    from rich import print

all_options = []
all_feedback = []
all_answers = []
q_descriptions = ['What is PYNQ?', 'Which of the following environments is meant to be used with PYNQ?',
                  'What are the the steps to get started with a PYNQ board?',
                  'With PYNQ, hardware system designs are referred to as:',
                  'What set of files are necessary to deploy a PYNQ system?',
                  'Fill in the blanks of these descriptions for Raspberry Pis, Arduinos, and FPGAs as discussed '
                  'in the workshop presentation. \n 1. A(n) __ is deployed close to hardware, and can be useful for '
                  'working with sensors and buttons. \n 2. A(n) __ runs an operating system (commonly Linux), '
                  'and acts like a little computer.\n 3. A(n) __ needs its architecture defined by the user.',
                  'What do you need to configure the logic circuit?',
                  'What does the Zynq system on a chip offer: select the appropriate options',
                  'What component on the board contains the PS/PL?',
                  'True or false: PYNQ offers Arduino and Raspberry Pi interfaces',
                  'Which command is used to install new PYNQ projects using hybrid packages?',
                  'Match these descriptions for FPGAs, (MP)SoCs, and ASICs \n 1. These are created for one '
                  'specific purpose. They are expensive to develop and manufacture, but they are very fast and '
                  'efficient. \n 2. An integrated circuit packaged with other components, like a processor or memory '
                  'components.\n 3. These devices cannot be used without being programmed, but are flexible and '
                  'relatively inexpensive to use. \n 4. An integrated circuit that is packaged with multiple '
                  'processing cores.', 'Which of these is not a hardware description language?',
                  'What do nanometers associated with an FPGA indicate?',
                  'Vivado is used to create hardware designs. Which of these things can you create with Vivado to '
                  'load onto your FPGA into order to configure the device?', 'What does FPGA stand for?',
                  'What does ASIC stand for?', 'What is the difference between Microprocessor and Microcontroller?',
                  'Select the ZYNQ Applications:', 'What languages does Jupyter support?',
                  'Label the image of the PYNQ board below with the appropriate interface name ###',
                  'Label the image of the PYNQ board below with the correct connection name ###']

options1 = ['A development board', 'An operating system', 'An open-source project and framework', 'A Python-based game']
ans1 = 'An open-source project and framework'
fb1 = ["[bold red]Not quite[/bold red]--a PYNQ board can be referred to as a development board, but this doesn\'t "
       "encompass all of what PYNQ is.",
       "[bold red]Incorrect[/bold red]--operating systems take care of a [black]computer\'s[/black] basic functions. "
       "Examples include various versions of Linux and Windows systems, and does not include PYNQ.",
       "[bold green]Correct![/bold green] PYNQ is a framework developed by Xilinx to integrate Python and Python based "
       "applications within an FPGA architecture. [black]\'PYNQ\'[/black] comes from Python + ZYNQ--Zynq referring to "
       "a "
       "specific FPGA architecture developed by Xilinx.",
       '[bold red]Incorrect[/bold red]--PYNQ is not a game, but you can certainly create one with the help of PYNQ.']

all_options.append(options1)
all_answers.append(ans1)
all_feedback.append(fb1)

options2 = ['PyCharm', 'Jupyter Notebooks', 'Visual Studio Code', 'BlueJ']
ans2 = 'Jupyter Notebooks'
fb2 = ['[bold red]Incorrect![/bold red] Python is a Python IDE (integrated development environment), but not the one '
       'that is readily installed with PYNQ.',
       '[bold green]Correct![/bold green] Jupyter Notebooks is already installed and usable on the PYNQ right out of '
       'the '
       'box. It\'s a cell-based coding environment that uses kernels to help you compile and run your (in this case, '
       'Python) code. With Jupyter Notebooks you can create .ipynb files or regular .py files. This quiz was built '
       'using '
       'Jupyter!',
       '[bold red]Incorrect![/bold red]Visual Studio Code is a popular code editor, but isn\'t as well suited for our '
       'purposes as another answer.',
       '[bold red]Incorrect![/bold red]BlueJ is a coding environment for the Java programming language, written in '
       'Java. '
       'Cool, but not appropriate for those coding in Python.']

all_options.append(options2)
all_answers.append(ans2)
all_feedback.append(fb2)

options3 = ['Plug the board into your computer for power, set the boot jumper to SD, and turn it on.',
            'Power the board, connect your computer to the board, turn it on, and load the PYNQ image onto the '
            'MicroSD with the OS on the device.',
            'Load PYNQ image onto MicroSD card, set the boot jumper, connect the board to power, connect computer to '
            'device, and turn it on.',
            'Set the boot jumper to SD, place the MicroSD with a pre-loaded PYNQ image in the device, and connect the '
            'board with Ethernet.']
ans3 = 'Load PYNQ image onto MicroSD card, set the boot jumper, connect the board to power, connect computer to ' \
       'device, and turn it on.'
fb3 = [
    '[bold red]Incorrect[/bold red] recall what is needed to start the board properly outside of the hardware setup.',
    '[bold red]Incorrect[/bold red] recall the order of the setup steps.',
    '[bold green]Correct![/bold green] Have the board setup instructions on hand so you don\'t forget any necessary '
    'steps.', '[bold red]Incorrect[/bold red] recall that you have to interact with the device through a computer.']

all_options.append(options3)
all_answers.append(ans3)
all_feedback.append(fb3)

options4 = ['APIs', 'Layers', 'Notebooks', 'Overlays']
ans4 = 'Overlays'
fb4 = ['[bold red]Incorrect![/bold red]An API (or [black]"Application Programming Interface"[/black]) is the software '
       'link between the user and the application. While this is the incorrect answer, and API is what allows you to '
       'interact with the correct answer.',
       '[bold red]Incorrect![/bold red]A [black]"layer"[/black] may refer to a [black]"layer"[/black] in an '
       'application '
       'software stack, among other things, but in this case, this is the incorrect answer.',
       '[bold red]Incorrect![/bold red]You may have first been exposed to Python or PYNQ through the use of iPython '
       'notebooks (like the one you\'re currently using), which provides an easy to use, cell-based coding '
       'environment.',
       '[bold green]Correct![/bold green] An PYNQ overlay is essentially a hardware design that is used to configure '
       'the '
       'architecture of your device as an FPGA.']

all_options.append(options4)
all_answers.append(ans4)
all_feedback.append(fb4)

options5 = ['Bitstream (*.bit),  Jupyter Notebook (*.ipynb)', 'Bitstream (*.bit), Hardware Handoff (*.hwh)',
            'Hardware Handoff (*.hwh), Jupyter Notebook (*ipynb)', ' Java Archive (*.jar), Text (.txt)']
ans5 = 'Bitstream (*.bit), Hardware Handoff (*.hwh)'
fb5 = ['[bold red]Close[/bold red]-- but you don\'t necessarily need a Jupyter notebook to deploy a PYNQ system, '
       'though those notebooks are used to interact with the device.',
       '[bold green]Correct![/bold green] The bitstream is what is loaded onto the device to configure its '
       'architecture. '
       'The hardware hand-off file contains a lot of information about the system on which your application is '
       'running--including info on clocks, IPs, and various system settings, among other things. Tip: You can also '
       'save '
       'the .tcl file created from Vivado to rebuild the hardware block diagram if necessary.',
       '[bold red]Close[/bold red]-- but you don\'t necessarily need a Jupyter notebook to deploy a PYNQ system, '
       'though those notebooks are used to interact with the device.',
       '[bold red]Not quite[/bold red]--recall what files are created in Vivado to work with the PYNQ framework.']

all_options.append(options5)
all_answers.append(ans5)
all_feedback.append(fb5)

options6 = ['FPGA, RPi, Arduino', 'FPGA, Arduino, RPi', 'Arduino, RPi, FPGA', 'RPi, FPGA, Arduino']
ans6 = 'Arduino, RPi, FPGA'
fb6_a = '[bold red]Try again![/bold red] Refer to the [black]"What is an FPGA?"[/black] notebook, the dropdown widget ' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        'above, or try to recall what best differentiates these devices from each other.'
fb6_b = '[bold green]Correct![/bold green] As we know, an FPGA\'s architecture is user defined through configuration, ' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        'while you can differentiate the RPi and Arduino microcontrollers through, for example, their proximity to ' \
        'peripherals, or specifying which is running an operating system.'
fb6 = [fb6_a, fb6_a, fb6_b, fb6_a]

all_options.append(options6)
all_answers.append(ans6)
all_feedback.append(fb6)

options7 = ['Load/program the logic circuit', 'Load/program the arm microprocessor',
            'Load/program the configuration memory layer in the FPGA', 'Load/program the ZYNQ 7020 chip']
ans7 = 'Load/program the configuration memory layer in the FPGA'
fb7_a = '[bold red]Incorrect[/bold red]'
fb7_b = '[bold red]Incorrect[/bold red]'
fb7_c = '[bold green]Correct[/bold green]'
fb7_d = '[bold red]Incorrect[/bold red]'
fb7 = [fb7_a, fb7_b, fb7_c, fb7_d]

all_options.append(options7)
all_answers.append(ans7)
all_feedback.append(fb7)

options8 = ['Arm Application microprocessor, real-time microcontroller', 'integrated programmable logic, Linux',
            'Arm Application microprocessor, real-time microcontroller, integrated programmable logic, Linux',
            'None of these features']
ans8 = 'Arm Application microprocessor, real-time microcontroller, integrated programmable logic, Linux'
fb8_a = '[bold red]Incorrect[/bold red]'
fb8_b = '[bold red]Incorrect[/bold red]'
fb8_c = '[bold green]Correct[/bold green]'
fb8_d = '[bold red]Incorrect[/bold red]'
fb8 = [fb8_a, fb8_b, fb8_c, fb8_d]

all_options.append(options8)
all_answers.append(ans8)
all_feedback.append(fb8)

options9 = ['ZYNQ 7020', 'XADC', 'The ARM microprocessor', 'Not on the board']
ans9 = 'ZYNQ 7020'
fb9_a = '[bold green]Correct[/bold green]'
fb9_b = '[bold red]Incorrect[/bold red]'
fb9_c = '[bold red]Incorrect[/bold red]'
fb9_d = '[bold red]Incorrect[/bold red]'
fb9 = [fb9_a, fb9_b, fb9_c, fb9_d]

all_options.append(options9)
all_answers.append(ans9)
all_feedback.append(fb9)

options10 = ['TRUE', 'FALSE']
ans10 = 'TRUE'
fb10_a = '[bold green]Correct[/bold green]'
fb10_b = '[bold red]Incorrect[/bold red]'
fb10 = [fb10_a, fb10_b]

all_options.append(options10)
all_answers.append(ans10)
all_feedback.append(fb10)

options11 = ['Conda install', 'PIP install', 'APT-get install', 'Easy-install']
ans11 = 'PIP install'
fb11_a = '[bold red]Try again[/bold red]. install conda sets up the environment, not a specific package'
fb11_b = '[bold green]Correct![/bold green] Pip can be used to install Python packages outside of a virtual ' \
         'environment like conda. '
fb11_c = '[bold red]Incorrect[/bold red], this command is used in Linux terminals, and is not used for PYNQ installs. '
fb11_d = '[bold red]Incorrect[/bold red]'
fb11 = [fb11_a, fb11_b, fb11_c, fb11_d]

all_options.append(options11)
all_answers.append(ans11)
all_feedback.append(fb11)

options12 = ['ASIC, SoC, FPGA, MPSoC', 'FPGA, SoC, ASIC, MPSoC', 'SoC, ASIC, FPGA, MPSoC', 'ASIC, MPSoC, FPGA, SoC']
ans12 = 'ASIC, SoC, FPGA, MPSoC'
fb12_a = '[bold green]Correct![/bold green] We know ASICs are application specific. The other three descriptions can ' \
         'apply to an FPGA, but you can determine the correct answer from the mention of other components and ' \
         'multiple processors.'
fb12_b = '[bold red]Incorrect![/bold red] Go back to the beginning of this notebook to review info on these four terms.'
fb12_c = '[bold red]Incorrect![/bold red] Go back to the beginning of this notebook to review info on these four terms.'
fb12_d = '[bold red]Incorrect![/bold red] Go back to the beginning of this notebook to review info on these four terms.'
fb12 = [fb12_a, fb12_b, fb12_c, fb12_d]

all_options.append(options12)
all_answers.append(ans12)
all_feedback.append(fb12)

options13 = ['Verilog', 'JHDL', 'Ruby', 'VHDL']
ans13 = 'Ruby'
fb13_a = '[bold red]Incorrect![/bold red] - look at the examples given in the notebook. Don\'t be afraid to look up a ' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         'language that looks unfamiliar to you.'
fb13_c = '[bold green]Correct![/bold green] Ruby is a high-level programming language that isn\'t used in designing ' \
         'hardware.'
fb13 = [fb13_a, fb13_a, fb13_c, fb13_a]

all_options.append(options13)
all_answers.append(ans13)
all_feedback.append(fb13)

options14 = ['The size of the FPGA', 'The size of a feature on an FPGA', 'The maximum routing distance between IP',
             'The physical size of a processor on an SoC']
ans14 = 'The size of a feature on an FPGA'
fb14_a = '[bold red]Incorrect![/bold red] remember that an FPGA is a silicon component.'
fb14_b = '[bold green]Correct![/bold green] An FPGA [black]\'feature\'[/black] refers to the elements on an FPGA, ' \
         'like a transistor, and smaller features means more can be fit in the same space, which is why you hear the ' \
         'number growing smaller as newer devices are developed. A higher number of features can imply (though not ' \
         'always) higher performance and power.'
fb14_c = '[bold red]Incorrect![/bold red] routing is not often measured and monitored in this way.'
fb14_d = '[bold red]Incorrect![/bold red] not all FPGA devices are SoCs.'
fb14 = [fb14_a, fb14_b, fb14_c, fb14_d]

all_options.append(options14)
all_answers.append(ans14)
all_feedback.append(fb14)

options15 = ['A .tcl script', 'An HDL file', 'An IP block', 'A bitstream']
ans15 = 'A bitstream'
fb15_a = '[bold red]Incorrect![/bold red] -a tcl script is used to rebuild your design, as it includes commands for ' \
         'Vivado to use.'
fb15_b = '[bold red]Incorrect![/bold red] - HDL is used when developing the hardware, but is not loaded into the ' \
         'device.'
fb15_c = '[bold red]Incorrect![/bold red] - IP are building blocks in your hardware design.'
fb15_d = '[bold green]Correct![/bold green] A bitstream is created based on your design, which is what is loaded onto ' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         '' \
         'the device in order for it to function as the designer intends.'
fb15 = [fb15_a, fb15_b, fb15_c, fb15_d]

all_options.append(options15)
all_answers.append(ans15)
all_feedback.append(fb15)

options16 = ['First Program Gate Array ', 'First Programmable Gate Array ', 'Field Programmable Gate Array',
             'Field Program Gate Array']
ans16 = 'Field Programmable Gate Array'
fb16_a = '[bold red]Incorrect![/bold red]'
fb16_b = '[bold red]Incorrect![/bold red]'
fb16_c = '[bold green]Correct.[/bold green]'
fb16_d = '[bold red]Incorrect![/bold red]'
fb16 = [fb16_a, fb16_b, fb16_c, fb16_d]

all_options.append(options16)
all_answers.append(ans16)
all_feedback.append(fb16)

options17 = ['Advanced Speed Integrated Circuit', 'Application Speedy Integrated Circuit',
             'Advanced Standard Integrated Circuit', 'Application Specific Integrated Circuit']
ans17 = 'Application Specific Integrated Circuit'
fb17_a = '[bold red]Incorrect![/bold red]'
fb17_b = '[bold red]Incorrect![/bold red]'
fb17_c = '[bold red]Incorrect![/bold red]'
fb17_d = '[bold green]Correct[/bold green]'
fb17 = [fb17_a, fb17_b, fb17_c, fb17_d]

all_options.append(options17)
all_answers.append(ans17)
all_feedback.append(fb17)

options18 = ['A  microprocessor is a programmable device which takes some input, performs some logical and arithmetic '
             'operations on it and \n produce some desired output. while A microcontroller is a computer which is '
             'typically '
             'dedicated to a single task. ',
             'A  microcontroller is a programmable device which takes some input, performs some logical and arithmetic '
             'operations on it and produce some desired output. while A microprocessor is a computer which is '
             'typically '
             'dedicated to a single task. ']
ans18 = 'A  microcontroller is a programmable device which takes some input, performs some logical and arithmetic ' \
        'operations on it and \n produce some desired output. while A microprocessor is a computer which is typically ' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        'dedicated to a single task. '
fb18_a = '[bold green]Correct.[/bold green] Microcontroller is like Arduino while Microprocessor is like Rasberry pi'
fb18_b = '[bold red]Incorrect![/bold red]'
fb18 = [fb18_a, fb18_b]

all_options.append(options18)
all_answers.append(ans18)
all_feedback.append(fb18)

options19 = ['Automotive driver assistance systems', 'Industrial control systems',
             'Remote robotic assisted surgery system', 'All of the above']
ans19 = 'All of the above'
fb19_a = '[bold red]Incorrect![/bold red]It\'s one of the applications but there are more'
fb19_b = '[bold red]Incorrect![/bold red]It\'s one of the applications but there are more'
fb19_c = '[bold red]Incorrect![/bold red]It\'s one of the applications but there are more'
fb19_d = '[bold green]Correct![/bold green] You got it'
fb19 = [fb19_a, fb19_b, fb19_c, fb19_d]

all_options.append(options19)
all_answers.append(ans19)
all_feedback.append(fb19)

options20 = ['C, Ruby, Python', 'Julia, Python, R', 'C++, Python', 'C, C++, C#']
ans20 = 'Julia, Python, R'
fb20_a = '[bold red]Incorrect![/bold red]'
fb20_b = '[bold green]Correct[/bold green]'
fb20_c = '[bold red]Incorrect![/bold red]'
fb20_d = '[bold red]Incorrect![/bold red]'
fb20 = [fb20_a, fb20_b, fb20_c, fb20_d]

all_options.append(options20)
all_answers.append(ans20)
all_feedback.append(fb20)

options21 = ['1. Raspberry Pi Interface, 2. Arduino Interfaces', '1. Arduino Interface, 2. Raspberry Pi Interfaces',
             '1.Pmod A interface, 2. Pmod B interfaces', '1.Pmod B interface, 2. Pmod A interfaces']
ans21 = '1. Raspberry Pi Interface, 2. Arduino Interfaces'
fb21_a = '[bold green]Correct[/bold green]'
fb21_b = '[bold red]Incorrect![/bold red]'
fb21_c = '[bold red]Incorrect![/bold red]'
fb21_d = '[bold red]Incorrect![/bold red]'
fb21 = [fb21_a, fb21_b, fb21_c, fb21_d]

all_options.append(options21)
all_answers.append(ans21)
all_feedback.append(fb21)

options22 = ['1.USB 2. SD Card 3. Ethernet 4. Pmod interfaces',
             '1. MicroUSB 2. MicroSD card 3. Ethernet  4. Raspberry Pi interfaces',
             '1. MicroUSB 2. MicroSD card 3. Ethernet  4. Pmod interfaces',
             '1.USB, 2. SD card 3. Ethernet 4. Arduino Interface']
ans22 = '1. MicroUSB 2. MicroSD card 3. Ethernet  4. Pmod interfaces'
fb22_a = '[bold red]Incorrect![/bold red]'
fb22_b = '[bold red]Incorrect![/bold red]'
fb22_c = '[bold green]Correct[/bold green]'
fb22_d = '[bold red]Incorrect![/bold red]'
fb22 = [fb22_a, fb22_b, fb22_c, fb22_d]

all_options.append(options22)
all_answers.append(ans22)
all_feedback.append(fb22)

ard_desc = 'An Arduino comes with a microcontroller. Unlike a Raspberry Pi, it does not have an operating system and ' \
           'can only run programs that were created and compiled specifically for Arduino boards, mostly written in ' \
           'C++. They\'re good for low-power applications and driving hardware, and are relatively easy to use, ' \
           'which has made them popular for robotics projects and teaching.'
rpi_desc = 'Raspberry Pis come with a microprocessor. They\'re pretty powerful, and have a variety of I/O ' \
           'options--with an RPi, you can use an SD cards, USB devices, HDMI displays, etc. You\'re also free to run ' \
           'it with almost any programming language.'
fpga_desc = 'FPGA stands for Field Programmable Gate Array. As you saw from the presentation, they are usable only ' \
            'after they\'ve been configured, creating a device whose architecture is customized for your task. This ' \
            'makes them efficient, adaptable, and useful for plenty of applications--medical devices, spacecrafts, ' \
            'self-driving cars, etc. Shown below is an evaluation board, with a Spartan-6 FPGA.'

platform_options = [('Arduino', 0), ('Raspberry Pi', 1), ('FPGA', 2)]
p_val = 0
p_desc = 'Platform'
platform_img_paths = ['images/arduino_uno.jpg', 'images/rpi.jpg', 'images/fpga.jpg']
plat_imgs = []
for k in platform_img_paths:
    file = open(k, "rb")
    image = file.read()

    plat_imgs.append(image)

platform_descs = [ard_desc, rpi_desc, fpga_desc]
platforms = widgets.Dropdown(options=platform_options, value=p_val, description=p_desc, disabled=False, )


# Use with an interact widget to create a dropdown menu that displays an image and description based on dropdown
# selection.
# dd_option: Dropdown input img_paths: list of image paths corresponding with index of dropdown selection
# desc_list: list of description strings corresponding with index of dropdown selection

def platform_dropdown(dd_option, img_wgs, desc_list):
    image = img_wgs[dd_option]
    desc = desc_list[dd_option]
    img = widgets.Image(value=image, format='png', width=300, align='center')
    display(Markdown('\n' + desc))
    display(img)
    return


def pop_platforms():
    t = widgets.interactive(platform_dropdown, desc_list=fixed(platform_descs), img_wgs=fixed(plat_imgs),
                            dd_option=platforms)
    return t


pynq_imgs_path = ['images/PynqLabel1.JPG', 'images/PynqLabel2.JPG']
pynq_imgs = []
for j in pynq_imgs_path:
    file = open(j, "rb")
    image = file.read()
    pynq_imgs.append(image)


def pynq_label_question(img_option, imgs):
    image = imgs[img_option]
    img = widgets.Image(value=image, format='png', width=300, align='center')
    display(img)


def pop_images(image_choice):
    t = widgets.interactive(pynq_label_question, imgs=fixed(pynq_imgs), img_option=fixed(image_choice))
    return t


def populate_questions():
    question_list = []
    for i in range(len(all_options)):
        question = [(q_descriptions[i]), show_buttons(all_options[i], all_answers[i], all_feedback[i])]
        if i == 5:
            platforms = pop_platforms()
            question.append(Markdown('#### Refer to the following dropdown widget for more info on each platform!'))
            question.append(platforms)
        if i == 20:
            img_choice = 0
            platforms = pop_images(img_choice)
            question.append(platforms)
        if i == 21:
            img_choice = 1
            platforms = pop_images(img_choice)
            question.append(platforms)
        question_list.append(question)
    return question_list


def show_buttons(options, answer, feedback):
    radios = RadioButtons(description=' ', options=options, disabled=False, layout={'width': 'max-content'})

    feedback_out = widgets.Output()
    checker = Button(description="Check")

    def submit(b):
        fb_text = feedback[options.index(radios.value)]
        with feedback_out:
            feedback_out.clear_output()
            print(fb_text)
        return

    checker.on_click(submit)

    return VBox([radios, checker, feedback_out])


questions = populate_questions()


def show_questions():
    display(Markdown('## Let\'s begin the test'))
    q = questions
    random.shuffle(q)
    for n, i in enumerate(q):
        if len(i) < 3:
            display(Markdown(f'### {n+1}. ' + i[0]))
            display(i[1])
        elif len(i) == 3:
            display(Markdown(f'### {n+1}. ' + i[0]))
            display(i[1], i[2])
        else:
            display(Markdown(f'### {n+1}. ' + i[0]))
            display(i[1], i[2], i[3])
    print(':tada: [bold]Congrats![/bold] :tada: You have completed the test!')
