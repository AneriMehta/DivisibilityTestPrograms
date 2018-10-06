function divisibleBy11(number){

    let par = 0;
    let impar = 0;

    if(number.length >= 2){

        let numbers = number.split('');
        for(let i = 0; i < number.length; i++){
            if(numbers[i] % 2 != 0){
                impar = impar + numbers[i];
            }else{
                par = par + numbers[i];
            }
        }

        number = par- impar;

        if(number === 0){
            return true;
        }
    }

    if(number % 11 === 0){
        return true
    }

    return false;
}

divisibleBy11(5863); // return true.