class Solution:
    def reconstructQueue(self, people):
        new_list = [None] * len(people)
        print(new_list)
        while people:
            min_value = 0
            for i in range(len(people)):
                if people[i][0] < people[min_value][0]:
                    min_value = i
                elif people[i][0] == min_value and people[i][1] < people[min_value][1]:
                    min_value = i

            if new_list[people[min_value][1]] == None:
                new_list[people[min_value][1]] = people[min_value]
            elif new_list[people[min_value][1]] != None:
                index = None
                for index in range(len(new_list)):
                        if new_list[index] == None:
                            index = index
                            break
                print(min_value,new_list[people[min_value][1]][1],people[min_value][1])

                find_position = False
                temp_position = people[min_value][1]
                smaller = 0
                while find_position == False:
                    if new_list[temp_position][0] > people[min_value][0]:
                        smaller += 1
                        if people[min_value][1] == smaller:
                        temp = new_list[temp_position]
                    print("!!!",temp_position)
                    if new_list[temp_position][1] > people[min_value][1]:
                        temp = new_list[temp_position]
                        new_list[temp_position] = people[min_value]
                        new_list[index] = temp
                        find_position = True
                        print("~~~",temp)
                    else:
                        temp_position += 1


            print(new_list)
            people.remove(people[min_value])
        return new_list

answer = Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
print(answer)