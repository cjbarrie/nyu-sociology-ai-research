import fs from 'node:fs';import {population,simulate} from '../research/model.mjs';
const version=process.argv[2]||'v2';const dir=`research/${version}`;fs.mkdirSync(dir,{recursive:true});
const reps=80;const scenarios=[['No chatbot',{access:0}],['Substitution',{bridging:0}],...(version==='v2'?[['Substitution + bridging',{bridging:.8}]]:[])];
const fields=['humanRequests','humanContacts','chatbot','noResponse'];
function summary(xs){const a=[...xs].sort((x,y)=>x-y);return {mean:xs.reduce((s,x)=>s+x,0)/xs.length,low:a[Math.floor(.025*(a.length-1))],high:a[Math.ceil(.975*(a.length-1))]}}
const results=scenarios.map(([name,parameters])=>({name,parameters,runs:[]}));
const grid=[];for(let si=0;si<=5;si++)for(let bi=0;bi<=(version==='v2'?5:0);bi++)grid.push({substitution:si/5,bridging:bi/5,changes:[]});
console.log(`MODEL ${version}: 100 people x 100 periods; ${reps} matched seeds.`);
console.log('Illustrative parameters, not estimates. Bands are run-to-run variation.');
for(let seed=1;seed<=reps;seed++){
 const world=population(seed);const baseline=simulate(world,{access:0});
 for(const r of results){const x=simulate(world,r.parameters);r.runs.push(Object.fromEntries(fields.map(f=>[f,100*x[f]/x.needs])))}
 for(const g of grid){const x=simulate(world,g);g.changes.push(100*(x.humanRequests-baseline.humanRequests)/x.needs)}
 if(seed%20===0)console.log(`Completed seed ${seed}/${reps}`);
}
const data={version,reps,n:100,periods:100,unit:'events per 100 support needs',scenarios:results.map(r=>({name:r.name,parameters:r.parameters,metrics:Object.fromEntries(fields.map(f=>[f,summary(r.runs.map(x=>x[f]))]))})),grid:grid.map(g=>({substitution:g.substitution,bridging:g.bridging,...summary(g.changes)}))};
fs.writeFileSync(`${dir}/results.json`,JSON.stringify(data,null,2));
const rows=['scenario,seed,'+fields.join(',')];for(const r of results)r.runs.forEach((x,i)=>rows.push([r.name,i+1,...fields.map(f=>x[f])].join(',')));fs.writeFileSync(`${dir}/runs.csv`,rows.join('\n'));
for(const s of data.scenarios)console.log(`${s.name}: ${s.metrics.humanRequests.mean.toFixed(1)} human requests / 100 needs`);
fs.copyFileSync('research/model.mjs',`${dir}/model.mjs`);console.log(`Saved ${dir}/results.json, runs.csv and model.mjs`);
