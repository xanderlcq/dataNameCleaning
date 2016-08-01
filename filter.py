import json
import re

def get_digits_length(inputs,index):
    length = 0
    while index+length < len(inputs):
        if inputs[index+length].isdigit():
            length+=1
        else:
            return length
    return length

f = open('china-mapbar-life-160613–20160721_name_error_new')
lines = f.readlines()
jsons = []
for line in lines:
    jsons.append(json.loads(line))


for e in jsons:
    # remove NO.
    if 'NO' in e['name']:
        if e['name'][e['name'].index('NO')-1] == '(':
            e['name'] = e['name'][:e['name'].index('NO')-1]
        else:
            e['name'] = e['name'][:e['name'].index('NO')]
        #print(e['name'])
    # remove no.
    if 'no' in e['name']:
        if e['name'][e['name'].index('no') - 1] == '(':
            e['name'] = e['name'][:e['name'].index('no') - 1]
        else:
            e['name'] = e['name'][:e['name'].index('no')]
        #print(e['name'])
    if 'No' in e['name']:
        if e['name'][e['name'].index('No') - 1] == '(':
            e['name'] = e['name'][:e['name'].index('No') - 1]
        else:
            e['name'] = e['name'][:e['name'].index('No')]
                # print(e['name'])
    if '玫琳凯授权经销商工作室' in e['name']:
        e['name'] = '玫琳凯授权经销商工作室'

    # Phone Number (8 or 11 digits)
    m = re.search('\d',e['name'])
    if m:
        # not 4S or 4s or special stuff
        if e['name'][m.start():m.start()+2] !='4S' and e['name'][m.start():m.start()+2] !='4s' and e['name'][m.start():m.start()+5] !='95081' and e['name'][m.start():m.start()+5] !='12356' :
            if get_digits_length(e['name'],m.start()) == 8 or get_digits_length(e['name'],m.start()) == 11:
                e['name'] = e['name'][:m.start()]+e['name'][m.start()+get_digits_length(e['name'],m.start()):]
                #print(e['name'])
        else:
            if e['name'] != '361°':
                if '4S' in e['name']:
                    n = re.search('\d',e['name'][e['name'].index('4S')+1:])
                    if n:
                        print(e['name'])
                        user_in = input('Change to:\n')
                        if user_in != '':
                            e['name'] = user_in
                if '4s' in e['name']:
                    n = re.search('\d', e['name'][e['name'].index('4s') + 1:])
                    if n:
                        print(e['name'])
                        user_in = input('Change to:\n')
                        if user_in != '':
                            e['name'] = user_in

            """
            print(e['name'])
            user_in = input('Change to:\n')
            if user_in!='':
                e['name']=user_in
            """
    # remove 师傅
    if '师傅' in e['name']:
        e['name'] = e['name'][:e['name'].index('师傅')-1]
        #print(e['name'])

    # remove ()
    if '()' in e['name']:
        e['name'] = e['name'][:e['name'].index('()')]
    #print(e['name'])


for e in jsons:
    if '4S' in e['name']:
        m = re.search('\d', e['name'][e['name'].index('4S'):])
        if m:
            if get_digits_length(e['name'], m.start()) == 8 or get_digits_length(
                    e['name'], m.start()) == 11:
                e['name'] = e['name'][:m.start()] + e['name'][
                                                    m.start() + get_digits_length(e['name'], m.start()):]
    if '4s' in e['name']:
        m = re.search('\d', e['name'][e['name'].index('4s'):])
        if m:
            if get_digits_length(e['name'], m.start()) == 8 or get_digits_length(
                    e['name'], m.start()) == 11:
                e['name'] = e['name'][:m.start()] + e['name'][
                                                  m.start() + get_digits_length(e['name'], m.start()):]
    """if '(' in e['name']:
        print(e['name'],'(*)')
        user_in = input('Change to:\n')
        if user_in == '':
            e['name'] = e['name'][:e['name'].index('(')]
        else:
            e['name'] = user_in"""


for e in jsons:
    # re-find all not '4S' '4s' item with digits in it
    m = re.search('\d', e['name'])
    if m:
        # not 4S or 4s or special stuff
        if e['name'][m.start():m.start() + 2] != '4S' and e['name'][
                                                          m.start():m.start() + 2] != '4s' and \
                        e['name'][m.start():m.start() + 5] != '95081' and e[
                                                                              'name'][
                                                                          m.start():m.start() + 5] != '12356':
            if e['name']!='361°':
                print(e['name'])
                user_in = input('Change to:\n')
                if user_in != '':
                    e['name'] = user_in
with open('pros1', 'a') as outfile:
    for hostDict in jsons:
        json.dump(hostDict, outfile,ensure_ascii=False)
        outfile.write('\n')