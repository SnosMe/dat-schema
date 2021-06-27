
type TalismanMonsterMods {
  _: i32
  _: i32
  _: rid
}

type TalismanPacks {
  Id: string
  MonsterPacksKeys: [MonsterPacks]
  _: i32
  _: i32
  MonsterVarietiesKey: MonsterVarieties
  _: i32
  _: i32
  _: i32
  _: i32
  MonsterPacksKey: MonsterPacks
}

type Talismans {
  BaseItemTypesKey: BaseItemTypes @unique
  SpawnWeight: i32
  ModsKey: Mods
  Tier: i32
  _: bool
  _: bool
  _: rid
  _: rid
  _: i32
}