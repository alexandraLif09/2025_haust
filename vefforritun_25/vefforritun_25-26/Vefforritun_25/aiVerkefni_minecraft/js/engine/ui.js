export class UI{
on(ev,fn){ this.events[ev]=fn }
emit(ev,...a){ this.events[ev]?.(...a) }


setupHotbar(){
this.toolbar.forEach((el,i)=>{
el.addEventListener('click', ()=>{
this.toolbar.forEach(t=>t.classList.remove('active'))
el.classList.add('active')
const id = el.dataset.block
this.holder = id
this.emit('selectBlock', id)
})
})
window.addEventListener('wheel', (e)=>{
if(e.deltaY>0) this.hotIndex = (this.hotIndex+1)%this.toolbar.length
else this.hotIndex = (this.hotIndex-1+this.toolbar.length)%this.toolbar.length
this.toolbar.forEach(t=>t.classList.remove('active'))
const el = this.toolbar[this.hotIndex]
el.classList.add('active')
this.emit('selectBlock', el.dataset.block)
})
}


setupButtons(){
this.toggleWire.addEventListener('click', ()=>this.emit('toggleWire'))
this.resetBtn.addEventListener('click', ()=>this.emit('reset'))
}


start(){
// simple minimap render using renderer copy (tiny trick)
const mm = document.getElementById('minimap')
const ctx = mm.getContext?.('2d')
if(!ctx) return
const loop = ()=>{
// draw simple crosshair
ctx.clearRect(0,0,mm.width,mm.height)
ctx.fillStyle = 'rgba(255,255,255,0.06)'
ctx.fillRect(0,0,mm.width,mm.height)
ctx.fillStyle = '#7be495'
ctx.fillRect(mm.width/2-2, mm.height/2-8,4,16)
ctx.fillRect(mm.width/2-8, mm.height/2-2,16,4)
requestAnimationFrame(loop)
}
requestAnimationFrame(loop)
}
}