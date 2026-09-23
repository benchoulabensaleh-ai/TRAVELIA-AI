"use client";
import {useState} from "react";
const API=process.env.NEXT_PUBLIC_API_URL||"http://localhost:8000";
type Item={time:string;title:string;category:string;duration_minutes:number;estimated_cost:number;indoor?:boolean;reason?:string};

export default function Home(){
 const [days,setDays]=useState<Item[][]>([]);
 const [message,setMessage]=useState("Tell me about your trip and I will build the first plan.");
 const [busy,setBusy]=useState(false);
 async function createPlan(){
  setBusy(true);
  const r=await fetch(`${API}/api/travel/itinerary`,{method:"POST",headers:{"Content-Type":"application/json"},
   body:JSON.stringify({destination:"Dubai",days:2,budget:800,currency:"USD",interests:["culture","food","outdoor"],dietary_preferences:["halal"],avoid_crowds:true,travel_style:"relaxed"})});
  const d=await r.json(); setDays(d.days); setMessage("Your personalized Dubai itinerary is ready."); setBusy(false);
 }
 async function replan(){
  if(!days.length)return; setBusy(true);
  const itinerary={destination:"Dubai",days,total_estimated_cost:days.flat().reduce((s,x)=>s+x.estimated_cost,0),assumptions:[]};
  const r=await fetch(`${API}/api/travel/replan`,{method:"POST",headers:{"Content-Type":"application/json"},
   body:JSON.stringify({itinerary,weather_condition:"heavy rain",rain_probability:80,current_day:1,remaining_budget:800})});
  const d=await r.json(); setDays(d.days); setMessage("Weather changed. TRAVELIA automatically replanned the trip."); setBusy(false);
 }
 return <main className="min-h-screen p-6 md:p-10"><div className="mx-auto max-w-7xl">
  <header className="mb-8 flex items-center justify-between"><div><div className="text-2xl font-bold">TRAVELIA</div><div className="text-sm text-slate-400">Your journey. Your voice. Your trip adapts.</div></div><div className="rounded-full border border-white/10 bg-white/5 px-4 py-2">Dubai · 48 hours</div></header>
  <section className="grid gap-6 lg:grid-cols-[1fr_1.4fr]">
   <div className="rounded-3xl border border-white/10 bg-white/5 p-6"><div className="mb-3 text-sm text-slate-400">VOICE CONCIERGE</div><div className="min-h-40 rounded-2xl bg-black/20 p-5 text-lg leading-8">{message}</div>
    <button onClick={createPlan} disabled={busy} className="mt-5 w-full rounded-2xl bg-white px-5 py-4 font-semibold text-slate-950">{busy?"Working...":"🎙️ Build my Dubai trip"}</button>
    <button onClick={replan} disabled={busy||!days.length} className="mt-3 w-full rounded-2xl border border-white/15 px-5 py-4 font-semibold">🌧️ Simulate weather change</button>
   </div>
   <div className="rounded-3xl border border-white/10 bg-white/5 p-6"><div className="mb-5 flex justify-between"><div><div className="text-sm text-slate-400">TODAY'S JOURNEY</div><div className="text-2xl font-semibold">Adaptive itinerary</div></div><div className="text-right text-sm">🌤️ 31°C</div></div>
    <div className="space-y-3">{(days[0]||[]).map((x,i)=><div key={i} className="rounded-2xl border border-white/10 bg-black/20 p-4"><div className="flex gap-4"><div className="w-14 text-sm text-slate-400">{x.time}</div><div><div className="font-semibold">{x.title}</div><div className="mt-1 text-sm text-slate-400">{x.category} · {x.duration_minutes} min · ${x.estimated_cost}</div>{x.reason&&<div className="mt-2 text-sm">↻ {x.reason}</div>}</div></div></div>)}{!days.length&&<div className="py-20 text-center text-slate-500">Your itinerary will appear here.</div>}</div>
   </div>
  </section>
 </div></main>
}
