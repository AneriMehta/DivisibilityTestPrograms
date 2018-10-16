function divide_by_16(value)
    result = value/16
    if result == math.floor(result) then
        return true
    end
    return false
end

for val=1,100 do
    print(string.format("%d divisible by 16?: %s",val,divide_by_16(val)))
end
