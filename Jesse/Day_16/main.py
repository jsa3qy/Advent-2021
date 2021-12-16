from timeit import default_timer as timer

hex_map = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}

version_count = 0

def parse_sub(input):
    global version_count
    version = input[:3]
    type_id = input[3:6]
    version_count += int(version,2)
    if int(type_id,2) == 4:
        return parse_literal(input[6:])
    elif int(type_id,2) != 4:
        length_type_id = input[6]
        total_length_of_subpackets = None
        num_subpackets = None

        if length_type_id == "0":
            total_length_of_subpackets = int(input[7:22],2)
            rest = input[22:]
        elif length_type_id == "1":
            num_subpackets = int(input[7:18], 2)
            rest = input[18:]

        if total_length_of_subpackets != None:
            bit_count = 0
            values = []
            while bit_count < total_length_of_subpackets:
                value,bit_addition,_ = parse_sub(rest)
                values.append(value)
                bit_count += bit_addition
                rest = rest[bit_addition:]
                if len(rest)*"0" == rest:
                    bit_count = total_length_of_subpackets
            return result_type(type_id, values), total_length_of_subpackets + 22, version_count
        elif num_subpackets != None:
            bit_count = 0
            values = []
            for _ in range(num_subpackets):
                value,cur_pos,_ = parse_sub(rest)
                values.append(value)
                bit_count += cur_pos
                rest = rest[cur_pos:]
                if len(rest)*"0" == rest:
                    break
            return result_type(type_id, values), bit_count + 18, version_count
        return None, 0, _
    
def result_type(type_id, values):
    if int(type_id,2) == 0 or int(type_id,2) == 4:
        result = sum(values)
    elif int(type_id,2) == 1:
        result = 1
        for val in values:
            result *= val
    elif int(type_id,2) == 2:
        result = min(values)
    elif int(type_id,2) == 3:
        result = max(values)
    elif int(type_id,2) == 5:
        if values[0] > values[1]:
            result = 1
        else:
            result = 0
    elif int(type_id,2) == 6:
        if values[0] < values[1]:
            result = 1
        else:
            result = 0
    elif int(type_id,2) == 7:
        if values[0] == values[1]:
            result = 1
        else:
            result = 0
    return result

def parse_literal(input):
    chunks = [input[i:i+5] for i in range(0, len(input), 5)]
    final_val = ""
    num_chunks = 0
    for chunk in chunks:
        final_val += chunk[1:]
        num_chunks += 1
        if chunk[0] == "0":
            break
    offset_of_literal = 6 + 5*num_chunks
    return int(final_val, 2), offset_of_literal, version_count

if __name__ == "__main__":
    start = timer()
    part_2,_,part_1 = parse_sub("".join([hex_map[char] for char in "020D74FCE27E600A78020200DC298F1070401C8EF1F21A4D6394F9F48F4C1C00E3003500C74602F0080B1720298C400B7002540095003DC00F601B98806351003D004F66011148039450025C00B2007024717AFB5FBC11A7E73AF60F660094E5793A4E811C0123CECED79104ECED791380069D2522B96A53A81286B18263F75A300526246F60094A6651429ADB3B0068937BCF31A009ADB4C289C9C66526014CB33CB81CB3649B849911803B2EB1327F3CFC60094B01CBB4B80351E66E26B2DD0530070401C82D182080803D1C627C330004320C43789C40192D002F93566A9AFE5967372B378001F525DDDCF0C010A00D440010E84D10A2D0803D1761045C9EA9D9802FE00ACF1448844E9C30078723101912594FEE9C9A548D57A5B8B04012F6002092845284D3301A8951C8C008973D30046136001B705A79BD400B9ECCFD30E3004E62BD56B004E465D911C8CBB2258B06009D802C00087C628C71C4001088C113E27C6B10064C01E86F042181002131EE26C5D20043E34C798246009E80293F9E530052A4910A7E87240195CC7C6340129A967EF9352CFDF0802059210972C977094281007664E206CD57292201349AA4943554D91C9CCBADB80232C6927DE5E92D7A10463005A4657D4597002BC9AF51A24A54B7B33A73E2CE005CBFB3B4A30052801F69DB4B08F3B6961024AD4B43E6B319AA020020F15E4B46E40282CCDBF8CA56802600084C788CB088401A8911C20ECC436C2401CED0048325CC7A7F8CAA912AC72B7024007F24B1F789C0F9EC8810090D801AB8803D11E34C3B00043E27C6989B2C52A01348E24B53531291C4FF4884C9C2C10401B8C9D2D875A0072E6FB75E92AC205CA0154CE7398FB0053DAC3F43295519C9AE080250E657410600BC9EAD9CA56001BF3CEF07A5194C013E00542462332DA4295680"]))
    print("Part 1: " + str(part_1) + " in " + str(timer() - start))
    print("Part 2: " + str(part_2) + " in " + str(timer() - start))