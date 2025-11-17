const listi = document.querySelector("#listi");
const allir = document.querySelector("#allir");
const nemendur = document.querySelector("#nemendur");
const kennarar = document.querySelector("#kennarar");

const people = [
    {
        id: 1,
        name: "Alex Hlyns",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Myndlistarbraut",
        status: "nemandi"
    },
    {
        id: 2,
        name: "Selma Jónsdóttir",
        school: "Setbergsskóli",
        course: "Íslenska",
        status: "kennari"
    },
    {
        id: 3,
        name: "Sibba Pálsdóttir",
        school: "Flensborgarskólinn",
        course: "Opin námsbraut - Félagslífssvið",
        status: "nemandi"
    },
    {
        id: 4,
        name: "Atli Rafnsson",
        school: "Setbergsskóli",
        course: "Náttúrufræði",
        status: "kennari"
    },
    {
        id: 5,
        name: "Freyja Wright",
        school: "Menntaskólinn við Hamrahlíð",
        course: "Félagsfræðibraut",
        status: "nemandi"
    },
    {
        id: 6,
        name: "Anna Kristín Jóhannesdóttir",
        school: "Setbergsskóli",
        course: "Enska",
        status: "kennari"
    },
    {
        id: 7,
        name: "Nadia Furtak",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Tölvubraut",
        status: "nemandi"
    },
    {
        id: 8,
        name: "Hilmar Halldórsson",
        school: "Grundaskóli",
        course: "Íslenska",
        status: "kennari"
    },
    {
        id: 9,
        name: "Elísabet Sigurjónsdóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Sjúkraliðabraut",
        status: "nemandi"
    },
    {
        id: 10,
        name: "Hjördís Dögg Grímarsdóttir",
        school: "Grundaskóli",
        course: "Íslenska",
        status: "kennari"
    },
    {
        id: 11,
        name: "Dagur Fannar Jóhannesson",
        school: "Menntaskólinn í Kópavogi",
        course: "Matreiðsla",
        status: "nemandi"
    },
    {
        id: 12,
        name: "Hlíf Árnadóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Íslenska",
        status: "kennari"
    },
    {
        id: 13,
        name: "Breki Páll Jónsson",
        school: "Menntaskólinn í Reykjavík",
        course: "Náttúrufræðibraut",
        status: "nemandi"
    },
    {
        id: 14,
        name: "Andrea Jónsdóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Stærðfræði",
        status: "kennari"
    },
    {
        id: 15,
        name: "Vigdís Helga Erlendsdóttir",
        school: "Verzlunarskóli Íslands",
        course: "Viðskipta hagfræði",
        status: "nemandi"
    },
    {
        id:16,
        name: "Vilborg Sverrisdóttir",
        school: "Hraunvallaskóli",
        course: "Íþróttir",
        status: "kennari"
    },
    {
        id: 17,
        name: "Rakel Sif Sigurðardóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Sjúkraliðabraut",
        status: "nemandi"
    }
];

const renderList = (list) => {
    listi.innerHTML = '';

    list.forEach(people => {

        let extraClass = '';
        if (people.status === 'nemandi') {
            extraClass = 'student'
        }
        const peopleHtml = `
            <article class = "folk ${extraClass}">
                <h3> ${people.name} </h3>
                <p> ${people.school} <p>
                <p> ${people.course} <p>
                <p> ${people.status} <p>
        `;
        listi.insertAdjacentHTML('beforeend', peopleHtml);
    });
};

allir.addEventListener('click', () => {
    renderList(people);
});

nemendur.addEventListener('click', () => {
    const nemandi = people.filter(p => p.status === 'nemandi');
    renderList(nemandi);
});

kennarar.addEventListener('click', () => {
    const kennari = people.filter(p => p.status === 'kennari');
    renderList(kennari);
});

renderList(people);