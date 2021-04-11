import { IBackground } from "Interface/IBackground";
import { Ability } from "./Ability";
import { Serializable } from "./Serializable";

export class Background extends Serializable implements IBackground {
    name: string;
    startingProficiencies: string[];
    abilities: Ability[];

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}