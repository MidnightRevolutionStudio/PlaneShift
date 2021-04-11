export enum ProficiencyLevel {
    None = 0,
    Proficient,
    Expertise
}

export interface IProficiency {
    name: string;
    level: number;
}
