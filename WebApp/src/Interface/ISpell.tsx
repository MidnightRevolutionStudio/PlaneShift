import { ICreature } from "./ICreature";

export interface ISpell {
    Cast(caster:ICreature,target:ICreature):void;
}