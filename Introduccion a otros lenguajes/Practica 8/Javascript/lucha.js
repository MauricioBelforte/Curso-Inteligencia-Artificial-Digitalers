class Combatant {
  constructor({ name, hp, strength, defense, speed, abilities = {} }) {
    this.name = name;
    this.maxHp = hp;
    this.hp = hp;
    this.strength = strength;
    this.defense = defense;
    this.speed = speed;
    this.abilities = abilities;
    this.alive = true;
  }

  // Recibe daño y aplica efectos de defensa, luego devuelve daño real recibido
  takeDamage(rawDamage) {
    if (!this.alive) return 0;
    // Reducción básica por defensa (no negativa)
    const damageAfterDef = Math.max(0, Math.round(rawDamage - this.defense * 0.5));
    this.hp -= damageAfterDef;
    if (this.hp <= 0) {
      this.hp = 0;
      this.alive = false;
    }
    return damageAfterDef;
  }

  // Método para curarse (usado por ciertas habilidades)
  heal(amount) {
    if (!this.alive) return 0;
    const healed = Math.min(amount, this.maxHp - this.hp);
    this.hp += healed;
    return healed;
  }

  // Ataque genérico: move debe tener { name, powerMult, type, special? }
  attack(target, move) {
    if (!this.alive) {
      console.log(`${this.name} no puede atacar: está fuera de combate.`);
      return;
    }
    if (!target.alive) {
      console.log(`${target.name} ya está fuera de combate.`);
      return;
    }

    console.log(`${this.name} usa ${move.name} contra ${target.name}.`);

    // cálculo base de daño
    const rand = Math.floor(Math.random() * 21); // 0..20 variación
    let baseDamage = Math.round(this.strength * (move.powerMult || 1) + rand);

    // efectos de habilidad del atacante
    if (move.name === 'heatVision' && this.abilities.heatVision?.armorPierce) {
      // ignora parte de la defensa del objetivo
      const pierce = this.abilities.heatVision.armorPierce; // e.g. 0.4 => ignora 40% de defensa
      const effectiveDefense = target.defense * (1 - pierce);
      baseDamage = Math.round(this.strength * (move.powerMult || 1) + rand + Math.max(0, (this.strength - effectiveDefense) * 0.2));
    }

    if (move.name === 'brutalStrike' && this.abilities.brutalStrike?.critChance) {
      // posible crítico
      const chance = Math.random();
      if (chance < this.abilities.brutalStrike.critChance) {
        baseDamage = Math.round(baseDamage * (1 + this.abilities.brutalStrike.critMult));
        console.log('¡Golpe crítico!');
      }
    }

    // efectos de defensa del objetivo (habilidades pasivas)
    if (target.abilities.invulnerable && Math.random() < target.abilities.invulnerable.chance) {
      // evade/parcial block
      const reduced = Math.round(baseDamage * target.abilities.invulnerable.reduction);
      console.log(`${target.name} reduce el daño gracias a su invulnerabilidad (${reduced} de daño reducido).`);
      baseDamage = Math.max(0, baseDamage - reduced);
    }

    // aplicar daño
    const damageDone = target.takeDamage(baseDamage);
    console.log(`${this.name} inflige ${damageDone} de daño a ${target.name}. (HP ${target.hp}/${target.maxHp})`);

    // efectos post-ataque (curación, sangrado, etc.)
    // ejemplo: Omni-Man regenera un poco tras atacar
    if (this.abilities.regeneration) {
      const healed = this.heal(this.abilities.regeneration.amount);
      if (healed > 0) console.log(`${this.name} regenera ${healed} HP tras el ataque. (HP ${this.hp}/${this.maxHp})`);
    }

    // ejemplo: calentamiento que puede causar daño adicional con el tiempo (no implementado aquí)
    return { damageDone, targetHp: target.hp, attackerHp: this.hp };
  }
}

/* --- Creamos a Superman y Omni-Man --- */

const superman = new Combatant({
  name: 'Superman',
  hp: 1200,
  strength: 140,
  defense: 90,
  speed: 95,
  abilities: {
    heatVision: { armorPierce: 0.35 }, // ignora 35% de la defensa enemiga en ese ataque
    invulnerable: { chance: 0.12, reduction: 0.5 }, // 12% prob de reducir 50% del daño entrante
    flight: true,
    superStrength: true
  }
});

const omniMan = new Combatant({
  name: 'Omni-Man',
  hp: 1300,
  strength: 160,
  defense: 75,
  speed: 88,
  abilities: {
    brutalStrike: { critChance: 0.18, critMult: 0.8 }, // 18% crítico que suma 80% daño
    regeneration: { amount: 30 }, // cura 30 HP tras cada ataque
    relentlessness: true
  }
});

/* --- Movimientos definidos (puedes añadir más) --- */
const moves = {
  heatVision: { name: 'heatVision', powerMult: 1.6, type: 'energy' },
  punch: { name: 'punch', powerMult: 1.0, type: 'physical' },
  brutalStrike: { name: 'brutalStrike', powerMult: 1.9, type: 'physical' },
  quickSlash: { name: 'quickSlash', powerMult: 0.9, type: 'physical' }
};

/* --- Ejemplo de combate: Superman ataca primero con heatVision --- */
console.log('--- COMBATE: Superman ataca Omni-Man con heatVision ---');
const resultado1 = superman.attack(omniMan, moves.heatVision);

/* Mostramos el estado de los objetos tras el ataque */
console.log('\nEstado tras ataque 1:');
console.log(JSON.stringify(superman, null, 2));
console.log(JSON.stringify(omniMan, null, 2));

/* --- Contraataque de Omni-Man con brutalStrike --- */
console.log('\n--- CONTRAATAQUE: Omni-Man usa brutalStrike ---');
const resultado2 = omniMan.attack(superman, moves.brutalStrike);

console.log('\nEstado final:');
console.log(JSON.stringify(superman, null, 2));
console.log(JSON.stringify(omniMan, null, 2));
