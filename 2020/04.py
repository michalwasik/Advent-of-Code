file = open('puzzle/04.in', 'r')
content = file.read().split("\n\n")

# part 1
def valid_check_v1(passport):
    if 'byr:' in passport and 'iyr:' in passport and 'eyr:' in passport and\
            'hgt:' in passport and 'hcl:' in passport and\
            'ecl:' in passport and 'pid:' in passport:
        return True


valid_passports = 0
for passport in content:
    if valid_check_v1(passport):
        valid_passports += 1
print(valid_passports)


# part 2
def valid_check_v2(passport):
    passport = passport.split()
    passport_dict ={}
    for category in passport:
        passport_dict[category.split(':')[0]] = category.split(':')[1]
    passport_dict['cid'] = 0
    if {'ecl', 'byr', 'iyr', 'pid', 'hgt', 'hcl', 'eyr', 'cid'} != set(passport_dict.keys()):
        return False
    else:
        def if_int(x):
            if x.isdigit():
                return int(x)
            else:
                return 0

        condition_to_pass = 0
        if 1919 < if_int(passport_dict['byr']) < 2003:
            condition_to_pass += 1
        if 2009 < if_int(passport_dict['iyr']) < 2021:
            condition_to_pass += 1
        if 2019 < if_int(passport_dict['eyr']) < 2031:
            condition_to_pass += 1
        if passport_dict['hgt'][-2:] == 'cm':
            if 149 < if_int(passport_dict['hgt'][:-2]) < 194:
                condition_to_pass += 1
        if passport_dict['hgt'][-2:] == 'in':
            if 58 < if_int(passport_dict['hgt'][:-2]) < 77:
                condition_to_pass += 1
        if len(passport_dict['hcl']) == 7 and passport_dict['hcl'][0] == '#':
            hcl_pass = 0
            for character in range(1, 7):
                if 96 < ord(passport_dict['hcl'][character]) < 103 or \
                        47 < ord(passport_dict['hcl'][character]) < 58:
                    hcl_pass += 1
                if hcl_pass == 6:
                    condition_to_pass += 1
        if passport_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            condition_to_pass += 1
        if len(passport_dict['pid']) == 9 and if_int(passport_dict['pid']) != 0:
            condition_to_pass += 1

        if condition_to_pass == 7:
            return True


valid_passports = 0
for passport in content:
    if valid_check_v2(passport):
        valid_passports += 1
print(valid_passports)
