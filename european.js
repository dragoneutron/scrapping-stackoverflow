const fs = require('fs');

let users = [];

for (let i = 1; i <= 2000; i++) {
    let content = fs.readFileSync(`dashboard/${i}.json`).toString();
    let data = JSON.parse(content);
    for (let user of data) users.push(user);
}

const isEuropean = location => {
    const keys = [
        'germany',
        'france',
        'poland',
        'switzerland',
        'denmark',
        'newzealand',
        'gm',
        'fr',
        'pl',
        'ch',
        'dk',
        'nz'
    ];

    for (let key of keys)
        if (location.toLowerCase().endsWith(key)) return true;

    return false;
};

let europeans = [];
for (let user of users)
    if (isEuropean(user.location)) europeans.push(user);

fs.writeFileSync('europeans.json', JSON.stringify(europeans, null, 2));