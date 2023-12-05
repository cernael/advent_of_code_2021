class Packet:

    def __init__(self, bits):
        self.version = int(bits[:3], 2)
        self.type = int(bits[3:6], 2)
        self.data, self.tail = self.parse_value(bits[6:]) if self.type == 4 else self.parse_data(bits[6:])

    def __repr__(self):
        if self.type == 4:
            return str([self.version, self.type, self.data])
        else:
            return str([self.version, self.type, [repr(p) for p in self.data]])

    def eval(self):
       if self.type == 4:
           return self.data

       subs = [p.eval() for p in self.data]

       if self.type == 0:
           return sum(subs)
       elif self.type == 1:
           acc = 1
           for t in subs:
               acc *= t
           return acc
       elif self.type == 2:
           return min(subs)
       elif self.type == 3:
           return max(subs)
       elif self.type == 5:
           return 1 if subs[0] > subs[1] else 0
       elif self.type == 6:
           return 1 if subs[0] < subs[1] else 0
       elif self.type == 7:
           return 1 if subs[0] == subs[1] else 0

    def vsum(self):
        vsum = self.version
        if self.type != 4:
            vsum += sum([p.vsum() for p in self.data])
        return vsum

    def parse_value(self, data):
        value = ''
        for i in range(0, len(data), 5):
            value += data[ i + 1 : i + 5 ]
            if data[i] == '0':
                return int(value, 2), data[i + 5:]
        return '', ''

    def parse_data(self, data):
        subs = []
        if data[0] == '0':
            l = int(data[ 1:16 ], 2)
            data, res = data[ 16:16+l ], data[16+ l: ]
            while data:
                packet = Packet(data)
                data = packet.tail
                subs.append(packet)
        else:
            n = int(data[1 : 12 ], 2)
            data = data[12:]
            while n:
                n -= 1
                packet = Packet(data)
                data = packet.tail
                subs.append(packet)
            res = data
        return subs,res


def solve(line):
    bits = bin(int('1'+line,16))[3:]

    p =  Packet(bits)

    return p.eval()

if __name__ == '__main__':
    lines = []
    with open('16.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print(solve(lines[0]))

    print('2021?', solve('D2FE28'))
    print('sum: 3', solve('C200B40A82'))
    print('product: 54', solve('04005AC33890'))
    print('min: 7', solve('880086C3E88112'))
    print('max: 9', solve('CE00C43D881120'))
    print('1', solve('D8005AC2A8F0'))
    print('0', solve('F600BC2D8F'))
    print('0', solve('9C005AC2F8F0'))
    print('1', solve('9C0141080250320F1802104A08'))
