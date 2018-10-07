function divide_by_9(value)
    result = value/9
    if result == math.floor(result) then
        return true
    end
    return false
end

for val=1,100 do
    print(string.format("%d divisible by 9?: %s",val,divide_by_9(val)))
end
