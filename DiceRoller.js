const { read } = require('fs');

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
die = "";
readline.question('Enter dice input (e.g. 2d6+3): ', input => {
    die = input;
    console.log("rolling " + die + " ...");
    console.log("You rolled a " + makeDie(die));
    readline.close();
});

function makeDie(die){
    sides = parseInt(die.substring(die.indexOf("d") + 1, die.indexOf("+")));
    numDie = parseInt(die.substring(0, die.indexOf("d")));
    if (die.indexOf("+") != -1) {
        mod = parseInt(die.substring(die.indexOf("+") + 1, die.length));
    }
    else if (die.indexOf("-") != -1) {
        mod = parseInt(die.substring(die.indexOf("-") + 1, die.length)) * -1;
    }
    else {
        mod = 0;
    }
    return rollDie(sides, numDie, mod);
}    
function rollDie(sides, numDie, mod) {
    let total = 0;
    for (let i = 0; i < numDie; i++) {
        total += Math.floor(Math.random() * sides) + 1;
    }
    total += mod;
    return total;
}

