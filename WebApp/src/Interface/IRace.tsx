import { IAttribute } from "./IAttribute";

export interface IRace {
    name: string;
    speed: number;
    attributeMods: IAttribute[];
    alignment: string;
    size: string;
}
