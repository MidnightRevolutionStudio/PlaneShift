import { ICreature } from "Interface/ICreature";
import { ISpell } from "Interface/ISpell";

export class Spell implements ISpell{
    Cast(caster: ICreature, target: ICreature): void {
        throw new Error("Method not implemented.");
    }
}