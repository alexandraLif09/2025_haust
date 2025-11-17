const listi = document.querySelector("#listi");
const allir = document.querySelector("#allir");
const nemendur = document.querySelector("#nemendur");
const kennarar = document.querySelector("#kennarar");

const students = [
    {
        id: 1,
        name: "Alex Hlyns",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Myndlistarbraut"
    },
    {
        id: 2,
        name: "Sibba Pálsdóttir",
        school: "Flensborgarskólinn",
        course: "Opin námsbraut - Félagslífssvið"
    },
    {
        id: 3,
        name: "Freyja Wright",
        school: "Menntaskólinn við Hamrahlíð",
        course: "Félagsfræðibraut"
    },
    {
        id: 4,
        name: "Nadia Furtak",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Tölvubraut"
    },
    {
        id: 5,
        name: "Elísabet Sigurjónsdóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Sjúkraliðabraut"
    },
    {
        id: 6,
        name: "Dagur Fannar Jóhannesson",
        school: "Menntaskólinn í Kópavogi",
        course: "Matreiðsla"
    },
    {
        id: 7,
        name: "Breki Páll Jónsson",
        school: "Menntaskólinn í Reykjavík",
        course: "Náttúrufræðibraut"
    },
    {
        id: 8,
        name: "Vigdís Helga Erlendsdóttir",
        school: "Verzlunarskóli Íslands",
        course: "Viðskipta hagfræði"
    },
    {
        id: 9,
        name: "Rakel Sif Sigurðardóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        course: "Sjúkraliðabraut"
    }
];

const teachers = [
    {
        id: 1,
        name: "Selma Jónsdóttir",
        school: "Setbergsskóli",
        subject: "Íslenska"
    },
    {
        id: 2,
        name: "Atli Rafnsson",
        school: "Setbergsskóli",
        subject: "Náttúrufræði"
    },
    {
        id: 3,
        name: "Anna Kristín Jóhannesdóttir",
        school: "Setbergsskóli",
        subject: "Enska"
    },
    {
        id: 4,
        name: "Hilmar Halldórsson",
        school: "Grundaskóli",
        subject: "Íslenska"
    },
    {
        id: 5,
        name: "Hjördís Dögg Grímarsdóttir",
        school: "Grundaskóli",
        subject: "Íslenska"
    },
    {
        id: 6,
        name: "Margrét Ákadóttir",
        school: "Grundaskóli",
        subject: "Aðstoðarskólstjóri"
    },
    {
        id: 7,
        name: "Hlíf Árnadóttir",
        school: "Fjölbrautarskólinn í Breiðholti",
        subject: "Íslenska"
    }
];

const renderList = (list) => {
    list.innerHTML = '';

    list.forEach(students => {

        let extraClass = '';
        if (students.school === 'Fjölbrautarskólinn í Breiðholti') {
            extraClass = 'FB';
        } else if (students.school === 'Flensborgarskólinn') {
            extraClass = 'Flens'
        } else if (students.school === 'Menntaskólinn við Hamrahlíð') {
            extraClass = 'MH'
        } else if (students.school === 'Menntaskólinn í Kópavogi') {
            extraClass = 'MK'
        } else if (students.school === 'Menntaskólinn í Reykjavík') {
            extraClass = 'MR'
        } else if (students.school === 'Verzlunarskóli Íslands') {
            extraClass = 'Verzlo'
        } else if (students.school === 'Setbergsskóli') {
            extraClass = 'Seto'
        } else if (students.school === 'Grundaskóli') {
            extraClass = 'Grundo'
        } 

        const studentsHtml = `
        <article class = "skoli ${extraClass}">
            <h3>${students.name}</h3>
            <p>${students.school}</p>
            <p>${students.course}<p>
        </article>
        `;

        listi.insertAdjacentHTML('beforeend', studentsHtml)
    });
};

allir.addEventListener('click', () => {
    renderList(students && teachers);
});