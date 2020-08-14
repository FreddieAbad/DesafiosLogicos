'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function regexVar() {
    // \b valida como palabra
    // (a|e|i|o|u) vocales
    // [a-z] valida minusculas
    // {2,} valida longitud
    // \1 valida primera letra
    // \b valida ultima letra
    let re = new RegExp(/\b(a|e|i|o|u)[a-z]{2,}\1\b/);
    return re;
}


function main() {
    const re = regexVar();
    const s = readLine();

    console.log(re.test(s));
}