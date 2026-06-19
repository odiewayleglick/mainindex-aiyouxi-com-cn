from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    note: str
    source_url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def display(self) -> str:
        base = f"关键词：{self.keyword}\n笔记：{self.note}"
        if self.source_url:
            base += f"\n来源：{self.source_url}"
        if self.tags:
            base += f"\n标签：{'、'.join(self.tags)}"
        base += f"\n创建时间：{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        if self.updated_at:
            base += f"\n更新时间：{self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}"
        return base

    def short_display(self) -> str:
        return f"[{self.keyword}] {self.note[:30]}{'...' if len(self.note) > 30 else ''}"


@dataclass
class KeywordNoteCollection:
    title: str
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> Optional[KeywordNote]:
        for note in self.notes:
            if note.keyword == keyword:
                return note
        return None

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [note for note in self.notes if tag in note.tags]

    def format_all(self) -> str:
        lines = [f"# {self.title}", f"共 {len(self.notes)} 条笔记", "=" * 40]
        for i, note in enumerate(self.notes, 1):
            lines.append(f"\n--- 第 {i} 条 ---")
            lines.append(note.display())
        return "\n".join(lines)

    def format_short_list(self) -> str:
        lines = [f"# {self.title}"]
        for note in self.notes:
            lines.append(note.short_display())
        return "\n".join(lines)


def demo_usage() -> None:
    collection = KeywordNoteCollection(title="游戏关键词笔记")

    note1 = KeywordNote(
        keyword="爱游戏",
        note="这是一个专注于游戏资讯与评测的网站，覆盖各类游戏平台。",
        source_url="https://mainindex-aiyouxi.com.cn",
        tags=["游戏", "资讯", "评测"]
    )

    note2 = KeywordNote(
        keyword="爱游戏攻略",
        note="提供热门游戏的详细攻略和技巧，帮助玩家快速上手。",
        source_url="https://mainindex-aiyouxi.com.cn/guide",
        tags=["游戏", "攻略", "技巧"]
    )

    note3 = KeywordNote(
        keyword="爱游戏社区",
        note="玩家交流讨论社区，可以分享游戏心得和组队信息。",
        source_url="https://mainindex-aiyouxi.com.cn/community",
        tags=["游戏", "社区", "交流"]
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)

    print(collection.format_all())
    print("\n" + "=" * 40)
    print("简短列表：")
    print(collection.format_short_list())

    print("\n" + "=" * 40)
    tag = "攻略"
    print(f"查找标签 '{tag}' 的笔记：")
    for note in collection.find_by_tag(tag):
        print(note.short_display())


if __name__ == "__main__":
    demo_usage()