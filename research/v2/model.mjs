/** Illustrative support-seeking ABM. Fixed network, no inference about people. */
export function rng(seed){let a=seed>>>0;return()=>{a+=0x6D2B79F5;let t=a;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return ((t^t>>>14)>>>0)/4294967296}}
export function population(seed=17,n=100,periods=100){
 const r=rng(seed); const agents=Array.from({length:n},(_,id)=>({id,access:r(),human:.35+.4*r(),need:.12+.16*r(),availability:.45+.4*r()}));
 const edges=[];const neighbors=Array.from({length:n},()=>[]);
 function edge(i,j){if(i===j||neighbors[i].includes(j))return;neighbors[i].push(j);neighbors[j].push(i);edges.push([i,j])}
 for(let i=0;i<n;i++){edge(i,(i+1)%n);edge(i,(i+2)%n);if(r()<.3)edge(i,Math.floor(r()*n))}
 const rounds=Array.from({length:periods},()=>({available:agents.map(()=>r()),events:agents.map(()=>({need:r(),human:r(),sub:r(),adopt:r(),bridge:r(),friend:r()}))}));
 return {seed,n,periods,agents,edges,neighbors,rounds};
}
export function simulate(world,{access=.8,substitution=.6,bridging=0,adoption=.65}={}){
 for(const [k,v] of Object.entries({access,substitution,bridging,adoption}))if(!(v>=0&&v<=1))throw new Error(`${k} must be in [0,1]`);
 const totals={needs:0,humanRequests:0,humanContacts:0,chatbot:0,noResponse:0,bridged:0};const history=[];
 for(let t=0;t<world.periods;t++){
 const frame=[];const round=world.rounds[t];
 for(const a of world.agents){const u=round.events[a.id];if(u.need>=a.need)continue;
 totals.needs++;const hasAI=a.access<access;const wantedHuman=u.human<a.human;
 const usesAI=hasAI&&(wantedHuman?u.sub<substitution:u.adopt<adoption);
 const bridge=usesAI && u.bridge<bridging; // v2: AI may prompt human outreach.
 const asksHuman=(wantedHuman&&!usesAI)||bridge;
 const friends=world.neighbors[a.id];const friend=friends[Math.floor(u.friend*friends.length)];
 const humanResponds=asksHuman&&round.available[friend]<world.agents[friend].availability;
 totals.humanRequests+=Number(asksHuman);totals.humanContacts+=Number(humanResponds);totals.chatbot+=Number(usesAI);totals.bridged+=Number(bridge);totals.noResponse+=Number(!usesAI&&!humanResponds);
 frame.push({from:a.id,to:asksHuman?friend:null,ai:usesAI,bridge,responded:humanResponds});
 }
 history.push({period:t+1,...totals,events:frame});
 }
 return {parameters:{access,substitution,bridging,adoption},...totals,history};
}
