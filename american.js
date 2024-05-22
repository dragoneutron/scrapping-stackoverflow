const fs = require('fs');

let users = [];

for (let i = 1; i <= 2000; i++) {
    let content = fs.readFileSync(`dashboard/${i}.json`).toString();
    let data = JSON.parse(content);
    for (let user of data) users.push(user);
}

const isAmerican = location => {
    const keys = [
        'us',
        'united states',
        'ca',
        'canada',
        'uk',
        'united kingdom'
    ];

    for (let key of keys)
        if (location.toLowerCase().endsWith(key)) return true;

    return false;
};

let americans = [];
for (let user of users)
    if (isAmerican(user.location)) americans.push(user);

fs.writeFileSync('americans.json', JSON.stringify(americans, null, 2));