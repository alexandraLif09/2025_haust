// Basic FPS-style controls: keyboard + pointer lock + collision-lite


// keyboard state
this.keys = {}


// pointer lock
dom.addEventListener('click', ()=>{
dom.requestPointerLock?.()
})


document.addEventListener('pointerlockchange', ()=>{
if(document.pointerLockElement) this.connected = true
else this.connected = false
})


// mouse look
document.addEventListener('mousemove', (e)=>{
if(!this.connected) return
const sensitivity = 0.002
this.camera.rotation.y -= e.movementX * sensitivity
this.camera.rotation.x -= e.movementY * sensitivity
this.camera.rotation.x = Math.max(-Math.PI/2 + 0.1, Math.min(Math.PI/2 - 0.1, this.camera.rotation.x))
})


// keyboard
window.addEventListener('keydown', (e)=>{this.keys[e.code]=true})
window.addEventListener('keyup', (e)=>{this.keys[e.code]=false})


// simple update loop
const loop = ()=>{
const dt = 1/60
this.update(dt)
requestAnimationFrame(loop)
}
requestAnimationFrame(loop)
}


connect(){ /* nothing else for now */ }


update(dt){
const forward = new THREE.Vector3(Math.sin(this.camera.rotation.y),0,Math.cos(this.camera.rotation.y)*1)
const right = new THREE.Vector3(Math.cos(this.camera.rotation.y),0,-Math.sin(this.camera.rotation.y))
forward.normalize(); right.normalize()
this.direction.set(0,0,0)
if(this.keys['KeyW']) this.direction.add(forward)
if(this.keys['KeyS']) this.direction.add(forward.clone().negate())
if(this.keys['KeyA']) this.direction.add(right.clone().negate())
if(this.keys['KeyD']) this.direction.add(right)


if(this.direction.length()>0) this.direction.normalize()
const move = this.direction.multiplyScalar(this.speed*dt)
this.camera.position.add(move)


if(this.keys['Space']) this.camera.position.y += 0.2 // jump-ish
// keep above ground
if(this.camera.position.y < 2) this.camera.position.y = 2


// ensure surrounding chunks exist
const cx = Math.floor(this.camera.position.x / this.engine.chunkSize)
const cz = Math.floor(this.camera.position.z / this.engine.chunkSize)
for(let dx=-1;dx<=1;dx++) for(let dz=-1;dz<=1;dz++) this.engine.ensureChunk(cx+dx, cz+dz)
}
}