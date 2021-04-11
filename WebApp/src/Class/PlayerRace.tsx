import { IRace } from "Interface/IRace";
import { Attribute } from "./Attribute";
import { Serializable } from "./Serializable";

export class PlayerRace extends Serializable implements IRace {
    name: string;
    speed: number;
    attributeMods: Attribute[];
    alignment: string;
    size: string;
    sizeDescription: string;
    age: string;
    subraces: string[];

    constructor(jsonStr: string) { super(jsonStr); }

    Serialize(): string {
        throw new Error("Method not implemented.");
    }
}
