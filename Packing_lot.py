class parking_lot(object):
    def __init__(self):
        self.parking_space = None

    def create_parking_space(self, size):
        self.parking_space = dict.fromkeys("{:1}".format(i) for i in range(1, size+1))
        print("Created a Parking lot of "+ str(size) + " spaces")

    def allocate_parking_space(self, reg_no, color):
        for k, v in self.parking_space.items():
            if v == None:
                self.parking_space[k] = [reg_no, color]
                print("Allocated slot number " + k)
                break
        else:
            print("No more packing space available")

    def deallocate_parking_space(self, slot_no):
        self.parking_space[slot_no] = None
        print("Parking space "+ slot_no+" is free")

    def status(self):
        print("slot no | registration no | colour")
        for k,v in self.parking_space.items():
            if v != None:
                print(k + " " + " ".join(v))

    def stats_for_slot_color(self,colour):
        lst = []
        for k,v in self.parking_space.items():
            if colour in v:
                lst.append(k)
        return lst

    def stats_for_slot_reg_no(self,reg_no):
        lst = []
        for k,v in self.parking_space.items():
            if reg_no in v:
                lst.append(k)
        return lst

    def stats_for_reg_colour(self,colour):
        lst = []
        for k,v in self.parking_space.items():
            if colour in v:
                lst.append(v[0])
        return lst


cont = True
if (initial := input(">> ")) == "./parking_lot":
    process = parking_lot()
    while(cont):
        com = input(">> ").split(' ')
        if com[0] == 'create':
            process.create_parking_space(int(com[1]))
        elif com[0] == 'park':
            process.allocate_parking_space(com[1],com[2])
        elif com[0] == 'leave':
            process.deallocate_parking_space(com[1])
        elif com[0] == 'status':
            process.status()
        elif com[0] == 'slot_number_for_cars_with_colour':
            print (process.stats_for_slot_color(str(com[1])))
        elif com[0] == 'slot_number_for_cars_with_reg_no':
            print (process.stats_for_slot_reg_no(str(com[1])))
        elif com[0] == 'reg_no_for_cars_with_colour':
            print (process.stats_for_reg_colour(str(com[1])))
        elif com[0] == 'quit':
            cont = False
        else:
            print("Invalid Command")
else:
    print("Invalid")
