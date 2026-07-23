#!/usr/bin/env python3
"""
Doom-Endpoint Convergence MMO Simulation
A standalone Flask app embedding a complete Simulonic MMO-style visualization
of the Doom-Endpoint Theory in relation to Null Unity / Infosophy.

Based on the AD–BC Metrics of the Doom–Endpoint Convergence Model
and its deep relation to Null Unity (collapse to ds² / ∅ as Maximal Informational Density).

Author: Generated for Hrishi Mukherjee / Simulon Research
"""

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Doom-Endpoint Convergence · Simulonic MMO Simulation</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
  
  * { margin: 0; padding: 0; box-sizing: border-box; }
  
  body {
    background: #000;
    color: #e0e0e0;
    font-family: 'Share Tech Mono', monospace;
    overflow: hidden;
    height: 100vh;
    width: 100vw;
  }
  
  #sim {
    display: block;
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(ellipse at center, #0a0a12 0%, #000000 70%);
  }
  
  #hud {
    position: absolute;
    top: 12px;
    left: 12px;
    z-index: 10;
    background: rgba(0, 0, 0, 0.72);
    border: 1px solid #333;
    border-left: 3px solid #c0392b;
    padding: 14px 18px;
    max-width: 340px;
    backdrop-filter: blur(6px);
    font-size: 13px;
    line-height: 1.45;
  }
  
  #hud h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 15px;
    color: #fff;
    letter-spacing: 1px;
    margin-bottom: 8px;
    text-shadow: 0 0 8px #c0392b;
  }
  
  #hud .metric {
    display: flex;
    justify-content: space-between;
    margin: 3px 0;
  }
  
  #hud .label { color: #888; }
  #hud .value { color: #fff; font-weight: bold; }
  #hud .ad { color: #e74c3c; }
  #hud .bc { color: #1abc9c; }
  #hud .pi { color: #f1c40f; }
  
  #progress {
    margin-top: 10px;
    height: 6px;
    background: #222;
    border-radius: 3px;
    overflow: hidden;
  }
  
  #progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #c0392b, #e74c3c, #fff);
    transition: width 0.3s;
  }
  
  #controls {
    position: absolute;
    bottom: 14px;
    left: 12px;
    z-index: 10;
    background: rgba(0,0,0,0.65);
    border: 1px solid #333;
    padding: 10px 14px;
    font-size: 12px;
    color: #aaa;
  }
  
  #controls kbd {
    background: #222;
    border: 1px solid #444;
    padding: 1px 5px;
    border-radius: 3px;
    color: #ddd;
    font-family: inherit;
  }
  
  #title {
    position: absolute;
    top: 12px;
    right: 16px;
    z-index: 10;
    text-align: right;
    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    color: #666;
    letter-spacing: 2px;
  }
  
  #title span {
    display: block;
    color: #aaa;
    font-size: 11px;
    margin-top: 2px;
  }
  
  #quote {
    position: absolute;
    bottom: 14px;
    right: 16px;
    z-index: 10;
    max-width: 380px;
    text-align: right;
    font-size: 11px;
    color: #555;
    line-height: 1.4;
    font-style: italic;
  }
  
  #status {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 20;
    font-family: 'Orbitron', sans-serif;
    font-size: 22px;
    color: #fff;
    text-shadow: 0 0 20px #c0392b, 0 0 40px #e74c3c;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.6s;
    text-align: center;
  }

  #lln-panel {
    position: absolute;
    top: 58px;
    right: 16px;
    z-index: 10;
    width: min(360px, calc(100vw - 32px));
    background: rgba(0, 0, 0, 0.78);
    border: 1px solid #333;
    border-right: 3px solid #f1c40f;
    padding: 12px 14px 13px;
    backdrop-filter: blur(7px);
    font-size: 11px;
    line-height: 1.35;
  }

  #lln-panel h2 {
    font-family: 'Orbitron', sans-serif;
    font-size: 12px;
    color: #fff;
    letter-spacing: 1.2px;
    margin-bottom: 2px;
  }

  #lln-panel .subtitle {
    color: #666;
    margin-bottom: 8px;
  }

  #llnChart {
    display: block;
    width: 100%;
    height: 142px;
    border: 1px solid #252525;
    background: rgba(5, 5, 8, 0.88);
  }

  .lln-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3px 14px;
    margin: 8px 0;
  }

  .lln-grid .metric {
    display: flex;
    justify-content: space-between;
    gap: 8px;
  }

  .lln-grid .label { color: #777; }
  .lln-grid .value { color: #eee; }

  .lln-control {
    display: grid;
    grid-template-columns: 84px 1fr auto;
    align-items: center;
    gap: 7px;
    margin-top: 6px;
    color: #777;
  }

  .lln-control select,
  .lln-control input {
    min-width: 0;
    accent-color: #f1c40f;
  }

  .lln-control select {
    grid-column: 2 / 4;
    width: 100%;
    color: #ddd;
    background: #111;
    border: 1px solid #333;
    padding: 3px 5px;
    font-family: inherit;
    font-size: 10px;
  }

  #targetP { width: 100%; }
  #targetPValue { color: #f1c40f; width: 44px; text-align: right; }

  .lln-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 5px;
    margin-top: 8px;
  }

  .lln-buttons button {
    border: 1px solid #3a3a3a;
    background: #151515;
    color: #bbb;
    padding: 5px 4px;
    font-family: inherit;
    font-size: 10px;
    cursor: pointer;
  }

  .lln-buttons button:hover,
  .lln-buttons button:focus {
    border-color: #f1c40f;
    color: #fff;
    outline: none;
  }

  #llnState {
    margin-top: 7px;
    color: #f1c40f;
    text-align: center;
    letter-spacing: 0.5px;
  }

  @media (max-width: 820px), (max-height: 720px) {
    #lln-panel {
      top: auto;
      right: 12px;
      bottom: 72px;
      width: min(330px, calc(100vw - 24px));
    }
    #llnChart { height: 104px; }
    #quote { display: none; }
  }
</style>
</head>
<body>
<canvas id="sim"></canvas>

<div id="hud">
  <h1>DOOM–ENDPOINT · NULL UNITY</h1>
  <div class="metric"><span class="label">Agents (Ψ)</span><span class="value" id="nTotal">0</span></div>
  <div class="metric"><span class="label">AD (Terminal)</span><span class="value ad" id="nAD">0</span></div>
  <div class="metric"><span class="label">BC (Alternatives)</span><span class="value bc" id="nBC">0</span></div>
  <div class="metric"><span class="label">Polarity Π</span><span class="value pi" id="pi">0.000</span></div>
  <div class="metric"><span class="label">Doom Intensity</span><span class="value" id="doom">0.00</span></div>
  <div class="metric"><span class="label">Absorbed (Null)</span><span class="value" id="absorbed">0</span></div>
  <div class="metric"><span class="label">Null Unity Progress</span><span class="value" id="nullPct">0%</span></div>
  <div id="progress"><div id="progress-bar"></div></div>
  <div style="margin-top:8px;font-size:11px;color:#666;">
    Target structural: 8:3 → Π = 5/11 ≈ +0.455<br>
    Endpoint limit: BC → 0 , Π → +1
  </div>
</div>

<div id="title">
  SIMULONIC MMO
  <span>Doom–Endpoint Convergence</span>
</div>

<section id="lln-panel" aria-label="Probability Mass Simulator">
  <h2>PROBABILITY MASS · LLN</h2>
  <div class="subtitle">Bernoulli AD/BC sampling → empirical mass convergence</div>
  <canvas id="llnChart" width="332" height="142"></canvas>
  <div class="lln-grid">
    <div class="metric"><span class="label">Samples n</span><span class="value" id="llnN">0</span></div>
    <div class="metric"><span class="label">Target P(AD)</span><span class="value ad" id="llnTarget">0.7273</span></div>
    <div class="metric"><span class="label">Mass AD</span><span class="value ad" id="llnAD">0.0000</span></div>
    <div class="metric"><span class="label">Mass BC</span><span class="value bc" id="llnBC">0.0000</span></div>
    <div class="metric"><span class="label">Absolute error</span><span class="value" id="llnError">—</span></div>
    <div class="metric"><span class="label">95% LLN band</span><span class="value" id="llnBand">—</span></div>
    <div class="metric"><span class="label">Empirical Π</span><span class="value pi" id="llnPi">0.0000</span></div>
    <div class="metric"><span class="label">AD / BC counts</span><span class="value" id="llnCounts">0 / 0</span></div>
  </div>
  <label class="lln-control">
    <span>Distribution</span>
    <select id="massPreset">
      <option value="structural">Structural 8:3 · 8/11</option>
      <option value="prior">Prior kernel · 72/121</option>
      <option value="asimila">Asimila · 88/141</option>
      <option value="endpoint">Endpoint limit · 1</option>
      <option value="custom">Custom probability</option>
    </select>
  </label>
  <label class="lln-control">
    <span>P(AD)</span>
    <input id="targetP" type="range" min="0" max="1" step="0.001" value="0.727">
    <output id="targetPValue">0.727</output>
  </label>
  <label class="lln-control">
    <span>Batch / tick</span>
    <input id="batchSize" type="range" min="1" max="500" step="1" value="50">
    <output id="batchSizeValue">50</output>
  </label>
  <div class="lln-buttons">
    <button id="llnToggle" type="button">PAUSE [L]</button>
    <button id="llnBurst" type="button">+1,000 [M]</button>
    <button id="llnReset" type="button">RESET MASS</button>
  </div>
  <div id="llnState">SAMPLING · WAITING FOR CONVERGENCE</div>
</section>

<div id="controls">
  <kbd>Click</kbd> spawn agent &nbsp;·&nbsp;
  <kbd>A</kbd> Asimila (BC boost) &nbsp;·&nbsp;
  <kbd>P</kbd> Endpoint Pulse &nbsp;·&nbsp;
  <kbd>L</kbd> LLN run/pause &nbsp;·&nbsp;
  <kbd>M</kbd> +1,000 mass &nbsp;·&nbsp;
  <kbd>R</kbd> Reset
</div>

<div id="quote">
  “Doom contracts alternatives, while the Endpoint converts that contraction into irreversible actuality.”<br>
  — AD–BC Metrics · Null Unity collapse to ∅ (MID)
</div>

<div id="status"></div>

<script>
(() => {
  const canvas = document.getElementById('sim');
  const ctx = canvas.getContext('2d');
  let W, H, CX, CY;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
    CX = W / 2;
    CY = H / 2;
  }
  window.addEventListener('resize', resize);
  resize();

  // ——— Simulation State ———
  const agents = [];
  let absorbed = 0;
  let doomIntensity = 0.15;
  let pulse = 0;
  let asimilaTimer = 0;
  let totalSpawned = 0;
  const TARGET_RATIO = 8 / 11; // structural AD share

  // ——— Probability Mass Simulator / Law of Large Numbers ———
  const MASS_PRESETS = {
    structural: { p: 8 / 11, label: 'Structural 8:3' },
    prior: { p: 72 / 121, label: 'Prior 72:49' },
    asimila: { p: 88 / 141, label: 'Asimila 88:53' },
    endpoint: { p: 1, label: 'Endpoint limit' }
  };

  class ProbabilityMassSimulator {
    constructor() {
      this.canvas = document.getElementById('llnChart');
      this.ctx = this.canvas.getContext('2d');
      this.targetP = TARGET_RATIO;
      this.preset = 'structural';
      this.batchSize = 50;
      this.running = true;
      this.accumulator = 0;
      this.tickSeconds = 0.05;
      this.history = [];
      this.bindControls();
      this.reset();
    }

    bindControls() {
      const preset = document.getElementById('massPreset');
      const target = document.getElementById('targetP');
      const batch = document.getElementById('batchSize');

      preset.addEventListener('change', () => {
        if (preset.value === 'custom') {
          this.preset = 'custom';
          this.targetP = Number(target.value);
          this.reset();
        } else {
          this.setPreset(preset.value);
        }
      });

      target.addEventListener('input', () => {
        this.preset = 'custom';
        preset.value = 'custom';
        this.targetP = Number(target.value);
        document.getElementById('targetPValue').textContent = this.targetP.toFixed(3);
        this.reset();
      });

      batch.addEventListener('input', () => {
        this.batchSize = Number(batch.value);
        document.getElementById('batchSizeValue').textContent = this.batchSize.toLocaleString();
      });

      document.getElementById('llnToggle').addEventListener('click', () => this.toggle());
      document.getElementById('llnBurst').addEventListener('click', () => {
        this.step(1000);
        flashStatus('PROBABILITY MASS BURST\n+1,000 Bernoulli trials');
      });
      document.getElementById('llnReset').addEventListener('click', () => this.reset());
    }

    setPreset(name) {
      const preset = MASS_PRESETS[name];
      if (!preset) return;
      this.preset = name;
      this.targetP = preset.p;
      document.getElementById('massPreset').value = name;
      document.getElementById('targetP').value = this.targetP;
      document.getElementById('targetPValue').textContent = this.targetP.toFixed(3);
      this.reset();
    }

    reset() {
      this.n = 0;
      this.adCount = 0;
      this.bcCount = 0;
      this.accumulator = 0;
      this.history = [{ n: 0, pHat: this.targetP }];
      this.updatePanel();
      this.draw();
    }

    sampleOne() {
      const type = Math.random() < this.targetP ? 'AD' : 'BC';
      this.n++;
      if (type === 'AD') this.adCount++;
      else this.bcCount++;
      this.record();
      this.updatePanel();
      return type;
    }

    step(count = this.batchSize) {
      let ad = 0;
      for (let i = 0; i < count; i++) {
        if (Math.random() < this.targetP) ad++;
      }
      this.n += count;
      this.adCount += ad;
      this.bcCount += count - ad;
      this.record();
      this.updatePanel();
    }

    record() {
      const pHat = this.n ? this.adCount / this.n : this.targetP;
      this.history.push({ n: this.n, pHat });
      if (this.history.length > 180) this.history.shift();
    }

    toggle() {
      this.running = !this.running;
      document.getElementById('llnToggle').textContent = this.running ? 'PAUSE [L]' : 'RUN [L]';
      this.updatePanel();
    }

    update(dt) {
      if (this.running) {
        this.accumulator += dt;
        while (this.accumulator >= this.tickSeconds) {
          this.step(this.batchSize);
          this.accumulator -= this.tickSeconds;
        }
      }
      this.draw();
    }

    get pHat() {
      return this.n ? this.adCount / this.n : 0;
    }

    get band95() {
      // Hoeffding: P(|p_hat-p| >= epsilon) <= 2 exp(-2 n epsilon²).
      return this.n ? Math.sqrt(Math.log(40) / (2 * this.n)) : 1;
    }

    updatePanel() {
      const pHat = this.pHat;
      const bcHat = this.n ? this.bcCount / this.n : 0;
      const error = this.n ? Math.abs(pHat - this.targetP) : null;
      const band = this.band95;
      const polarity = this.n ? 2 * pHat - 1 : 0;

      document.getElementById('llnN').textContent = this.n.toLocaleString();
      document.getElementById('llnTarget').textContent = this.targetP.toFixed(4);
      document.getElementById('llnAD').textContent = pHat.toFixed(4);
      document.getElementById('llnBC').textContent = bcHat.toFixed(4);
      document.getElementById('llnError').textContent = error === null ? '—' : error.toFixed(4);
      document.getElementById('llnBand').textContent = this.n ? '±' + band.toFixed(4) : '—';
      document.getElementById('llnPi').textContent = (polarity >= 0 ? '+' : '') + polarity.toFixed(4);
      document.getElementById('llnCounts').textContent =
        this.adCount.toLocaleString() + ' / ' + this.bcCount.toLocaleString();

      const state = document.getElementById('llnState');
      if (!this.running) {
        state.textContent = 'PAUSED · EMPIRICAL MASS HELD';
        state.style.color = '#888';
      } else if (!this.n) {
        state.textContent = 'SAMPLING · WAITING FOR CONVERGENCE';
        state.style.color = '#f1c40f';
      } else if (this.n >= 1000 && error <= 0.01) {
        state.textContent = 'CONVERGED · |P̂(AD) − P(AD)| ≤ 0.010';
        state.style.color = '#2ee6b8';
      } else if (error <= band) {
        state.textContent = 'WITHIN 95% HOEFFDING BAND';
        state.style.color = '#f1c40f';
      } else {
        state.textContent = 'OUTSIDE 95% BAND · CONTINUE SAMPLING';
        state.style.color = '#e74c3c';
      }
    }

    draw() {
      const canvas = this.canvas;
      const rect = canvas.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      const dpr = Math.min(2, window.devicePixelRatio || 1);
      const pixelW = Math.round(rect.width * dpr);
      const pixelH = Math.round(rect.height * dpr);
      if (canvas.width !== pixelW || canvas.height !== pixelH) {
        canvas.width = pixelW;
        canvas.height = pixelH;
      }

      const ctx = this.ctx;
      const w = rect.width;
      const h = rect.height;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, w, h);

      const left = 28;
      const right = w - 10;
      const top = 12;
      const bottom = h - 20;
      const plotW = right - left;
      const plotH = bottom - top;
      const y = p => bottom - Math.max(0, Math.min(1, p)) * plotH;

      // 95% finite-sample convergence band.
      if (this.n) {
        const hi = Math.min(1, this.targetP + this.band95);
        const lo = Math.max(0, this.targetP - this.band95);
        ctx.fillStyle = 'rgba(241, 196, 15, 0.07)';
        ctx.fillRect(left, y(hi), plotW, y(lo) - y(hi));
      }

      // Grid and theoretical mass line.
      ctx.lineWidth = 1;
      ctx.font = '9px "Share Tech Mono", monospace';
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      for (const level of [0, 0.5, 1]) {
        ctx.strokeStyle = level === 0.5 ? '#252525' : '#191919';
        ctx.beginPath();
        ctx.moveTo(left, y(level));
        ctx.lineTo(right, y(level));
        ctx.stroke();
        ctx.fillStyle = '#555';
        ctx.fillText(level.toFixed(1), left - 5, y(level));
      }

      ctx.setLineDash([5, 4]);
      ctx.strokeStyle = '#f1c40f';
      ctx.beginPath();
      ctx.moveTo(left, y(this.targetP));
      ctx.lineTo(right, y(this.targetP));
      ctx.stroke();
      ctx.setLineDash([]);

      // Empirical AD probability trajectory.
      if (this.history.length > 1) {
        ctx.strokeStyle = '#ff6b5a';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        this.history.forEach((point, i) => {
          const x = left + (i / (this.history.length - 1)) * plotW;
          if (i === 0) ctx.moveTo(x, y(point.pHat));
          else ctx.lineTo(x, y(point.pHat));
        });
        ctx.stroke();
      }

      // Current empirical BC mass as a terminal marker.
      if (this.n) {
        ctx.fillStyle = '#ff6b5a';
        ctx.beginPath();
        ctx.arc(right, y(this.pHat), 2.8, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#2ee6b8';
        ctx.beginPath();
        ctx.arc(right, y(1 - this.pHat), 2.3, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.textAlign = 'left';
      ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = '#777';
      ctx.fillText('P(AD)', left, h - 5);
      ctx.textAlign = 'right';
      ctx.fillText('n = ' + this.n.toLocaleString(), right, h - 5);
    }
  }

  const lln = new ProbabilityMassSimulator();

  // ——— Agent class ———
  class Agent {
    constructor(x, y, type, isPlayer = false) {
      this.x = x;
      this.y = y;
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = (Math.random() - 0.5) * 0.4;
      this.type = type; // 'AD' or 'BC'
      this.mass = 0.6 + Math.random() * 0.8;
      this.doom = type === 'AD' ? 0.3 + Math.random() * 0.4 : 0.05;
      this.life = 1.0;
      this.id = totalSpawned++;
      this.isPlayer = isPlayer;
      this.trail = [];
      this.hue = type === 'AD' ? 0 : 160; // red vs teal
    }

    update(dt) {
      const dx = CX - this.x;
      const dy = CY - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy) || 1;
      const nx = dx / dist;
      const ny = dy / dist;

      // Endpoint attractor potential V_i (stronger with doom & global intensity)
      let attract = (0.018 + doomIntensity * 0.04) * this.mass;
      if (this.type === 'AD') attract *= (1.4 + this.doom * 1.8);
      else attract *= (0.55 + (asimilaTimer > 0 ? 0.15 : 0));

      // BC diffusion / escape trajectories (∇²Ψ style kicks)
      if (this.type === 'BC' && Math.random() < 0.012) {
        this.vx += (Math.random() - 0.5) * 2.8;
        this.vy += (Math.random() - 0.5) * 2.8;
      }

      // Occasional branch split visual for BC
      if (this.type === 'BC' && Math.random() < 0.002 && agents.length < 90) {
        agents.push(new Agent(this.x + (Math.random()-0.5)*8, this.y + (Math.random()-0.5)*8, 'BC'));
      }

      // Force integration
      this.vx += nx * attract * dt * 60;
      this.vy += ny * attract * dt * 60;

      // Mild damping
      this.vx *= 0.985;
      this.vy *= 0.985;

      // Pulse of Endpoint absorption
      if (pulse > 0) {
        this.vx += nx * pulse * 0.8;
        this.vy += ny * pulse * 0.8;
      }

      this.x += this.vx * dt * 60;
      this.y += this.vy * dt * 60;

      // Trail
      this.trail.push({x: this.x, y: this.y});
      if (this.trail.length > 12) this.trail.shift();

      // Absorption into Endpoint (Null Unity collapse)
      if (dist < 18 + this.mass * 4) {
        absorbed++;
        this.life = 0;
        // Convert residual BC influence into AD polarity boost
        if (this.type === 'BC') doomIntensity = Math.min(1.8, doomIntensity + 0.012);
        else doomIntensity = Math.min(1.8, doomIntensity + 0.004);
        return false; // mark for removal
      }
      return true;
    }

    draw(ctx) {
      // Trail
      if (this.trail.length > 2) {
        ctx.beginPath();
        ctx.moveTo(this.trail[0].x, this.trail[0].y);
        for (let i = 1; i < this.trail.length; i++) {
          ctx.lineTo(this.trail[i].x, this.trail[i].y);
        }
        ctx.strokeStyle = this.type === 'AD'
          ? `rgba(231, 76, 60, ${0.15 + this.doom * 0.25})`
          : `rgba(26, 188, 156, 0.18)`;
        ctx.lineWidth = 1.2;
        ctx.stroke();
      }

      // Glow
      const r = 3 + this.mass * 2.2;
      const g = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, r * 3);
      if (this.type === 'AD') {
        g.addColorStop(0, `rgba(255, 180, 160, 0.9)`);
        g.addColorStop(0.4, `rgba(231, 76, 60, 0.5)`);
        g.addColorStop(1, 'rgba(231, 76, 60, 0)');
      } else {
        g.addColorStop(0, `rgba(180, 255, 230, 0.85)`);
        g.addColorStop(0.4, `rgba(26, 188, 156, 0.45)`);
        g.addColorStop(1, 'rgba(26, 188, 156, 0)');
      }
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(this.x, this.y, r * 3, 0, Math.PI * 2);
      ctx.fill();

      // Core
      ctx.beginPath();
      ctx.arc(this.x, this.y, r, 0, Math.PI * 2);
      ctx.fillStyle = this.type === 'AD' ? '#ff6b5a' : '#2ee6b8';
      ctx.fill();
    }
  }

  // ——— Initial population matching ~8:3 structural ratio ———
  function spawnInitial() {
    agents.length = 0;
    absorbed = 0;
    doomIntensity = 0.18;
    totalSpawned = 0;
    lln.reset();
    const N = 44;
    const R = Math.min(W, H) * 0.38;
    for (let i = 0; i < N; i++) {
      const a = (i / N) * Math.PI * 2 + Math.random() * 0.1;
      const rr = R * (0.85 + Math.random() * 0.3);
      const type = (i % 11 < 8) ? 'AD' : 'BC'; // exact 8:3 repeating
      agents.push(new Agent(CX + Math.cos(a) * rr, CY + Math.sin(a) * rr, type));
    }
  }

  // ——— Drawing Endpoint (Null Unity singularity / Focused-Staying) ———
  function drawEndpoint(ctx, t) {
    const baseR = 14 + Math.sin(t * 2.2) * 1.5;
    // Outer halo
    let g = ctx.createRadialGradient(CX, CY, 0, CX, CY, 90);
    g.addColorStop(0, 'rgba(255, 60, 40, 0.25)');
    g.addColorStop(0.3, 'rgba(200, 30, 20, 0.08)');
    g.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(CX, CY, 90, 0, Math.PI * 2);
    ctx.fill();

    // Core glow
    g = ctx.createRadialGradient(CX, CY, 0, CX, CY, baseR * 3);
    g.addColorStop(0, '#fff');
    g.addColorStop(0.15, '#ffccaa');
    g.addColorStop(0.4, '#e74c3c');
    g.addColorStop(1, 'rgba(180, 20, 10, 0)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(CX, CY, baseR * 3, 0, Math.PI * 2);
    ctx.fill();

    // Hard core
    ctx.beginPath();
    ctx.arc(CX, CY, baseR * 0.55, 0, Math.PI * 2);
    ctx.fillStyle = '#fff';
    ctx.fill();
  }

  // ——— HUD update ———
  function updateHUD() {
    const nAD = agents.filter(a => a.type === 'AD').length;
    const nBC = agents.filter(a => a.type === 'BC').length;
    const total = nAD + nBC;
    const pi = total > 0 ? (nAD - nBC) / total : 0;

    document.getElementById('nTotal').textContent = total;
    document.getElementById('nAD').textContent = nAD;
    document.getElementById('nBC').textContent = nBC;
    document.getElementById('pi').textContent = (pi >= 0 ? '+' : '') + pi.toFixed(3);
    document.getElementById('doom').textContent = doomIntensity.toFixed(2);
    document.getElementById('absorbed').textContent = absorbed;

    // Null Unity progress: how close we are to full absorption relative to initial + spawned
    const progress = Math.min(1, absorbed / (absorbed + total + 1));
    document.getElementById('nullPct').textContent = Math.round(progress * 100) + '%';
    document.getElementById('progress-bar').style.width = (progress * 100) + '%';
  }

  // ——— Status flash ———
  function flashStatus(msg) {
    const el = document.getElementById('status');
    el.textContent = msg;
    el.style.opacity = 1;
    setTimeout(() => { el.style.opacity = 0; }, 1800);
  }

  // ——— Interaction ———
  canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    // Agent classification is one observable draw from the active mass law.
    const type = lln.sampleOne();
    agents.push(new Agent(x, y, type, true));
  });

  window.addEventListener('keydown', (e) => {
    if (e.target instanceof Element && e.target.matches('input, select, button')) return;
    if (e.key === 'a' || e.key === 'A') {
      asimilaTimer = 180; // ~3 seconds of BC boost
      // Temporarily convert a few AD → BC (Asimila repair/cooperation)
      let converted = 0;
      for (const a of agents) {
        if (a.type === 'AD' && converted < 6 && Math.random() < 0.4) {
          a.type = 'BC';
          a.hue = 160;
          converted++;
        }
      }
      lln.setPreset('asimila');
      flashStatus('ASIMILA CORRECTION\n+BC repair / cooperation');
    }
    if (e.key === 'p' || e.key === 'P') {
      pulse = 2.8;
      lln.setPreset('endpoint');
      flashStatus('ENDPOINT PULSE\nTerminal absorption wave');
    }
    if (e.key === 'l' || e.key === 'L') {
      lln.toggle();
    }
    if (e.key === 'm' || e.key === 'M') {
      lln.step(1000);
      flashStatus('PROBABILITY MASS BURST\n+1,000 Bernoulli trials');
    }
    if (e.key === 'r' || e.key === 'R') {
      lln.setPreset('structural');
      spawnInitial();
      flashStatus('FIELD RESET\nNull Seed reconstituted');
    }
  });

  // ——— Main loop ———
  let last = performance.now();
  let t = 0;

  function frame(now) {
    const dt = Math.min(0.033, (now - last) / 1000);
    last = now;
    t += dt;

    // Decay
    if (pulse > 0) pulse *= 0.92;
    if (asimilaTimer > 0) asimilaTimer--;

    // Slow natural Doom growth (contraction of future-volume)
    doomIntensity = Math.min(1.85, doomIntensity + 0.00008 * agents.filter(a => a.type === 'AD').length);

    // Update agents
    for (let i = agents.length - 1; i >= 0; i--) {
      if (!agents[i].update(dt)) {
        agents.splice(i, 1);
      }
    }

    // Draw
    ctx.fillStyle = 'rgba(0, 0, 0, 0.22)'; // mild motion blur / trail persistence
    ctx.fillRect(0, 0, W, H);

    drawEndpoint(ctx, t);

    // Soft rays from a few AD agents toward Endpoint (visual motif of the cover)
    ctx.strokeStyle = 'rgba(231, 76, 60, 0.06)';
    ctx.lineWidth = 1;
    let rayCount = 0;
    for (const a of agents) {
      if (a.type === 'AD' && rayCount < 12 && Math.random() < 0.3) {
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(CX, CY);
        ctx.stroke();
        rayCount++;
      }
    }

    for (const a of agents) a.draw(ctx);

    updateHUD();
    lln.update(dt);

    // Endpoint limit message
    if (agents.length === 0 && absorbed > 20) {
      flashStatus('ENDPOINT ABSORPTION COMPLETE\nΠ → +1  ·  341_AD + 0_BC');
    }

    requestAnimationFrame(frame);
  }

  // Boot
  spawnInitial();
  flashStatus('DOOM–ENDPOINT FIELD INITIALIZED\n8 AD : 3 BC structural channels');
  requestAnimationFrame(frame);
})();
</script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {
        'status': 'ok',
        'model': 'Doom-Endpoint Convergence MMO',
        'polarity_target': '5/11',
        'probability_mass_simulator': 'law-of-large-numbers',
        'mass_presets': {
            'structural': '8/11',
            'prior': '72/121',
            'asimila': '88/141',
            'endpoint': '1',
        },
        'finite_sample_bound': 'Hoeffding 95%',
    }

if __name__ == '__main__':
    print("=" * 60)
    print("  DOOM–ENDPOINT CONVERGENCE  ·  SIMULONIC MMO")
    print("  AD–BC Metrics  ↔  Null Unity (∅ / ds²)")
    print("=" * 60)
    print("  Open http://127.0.0.1:5000")
    print("  Click to spawn · A = Asimila · P = Endpoint Pulse · L = LLN · M = +1,000 · R = Reset")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=False)
