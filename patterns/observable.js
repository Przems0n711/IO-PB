const dataElement = document.getElementById("data");
c1 = document.getElementById("c1");
c2 = document.getElementById("c2");
c3 = document.getElementById("c3");
c4 = document.getElementById("c4");
c5 = document.getElementById("c5");
c6 = document.getElementById("c6");

// PROVIDER
const {fromEvent, operators} = rxjs;
const {map} = operators;

const keyup$ = fromEvent(dataElement, "keyup");

const normalStearm$ = keyup$.pipe(
    map(event => event.target.value)
);

const upperCaseStream$ = normalStearm$.pipe(
    map(value => value.toUpperCase())
);

// CONSUMER


normalStearm$.subscribe((value) => {
    c1.InnerText = value;
});

upperCaseStream$.subscribe(event => {
    console.log(event);
    
});
