# Cài và dùng skill

Skill nằm trọn trong `skills/hook-script/`. Sao chép **cả thư mục**, gồm `SKILL.md` và `references/`. Repo không cần npm, Python hay API key để đọc nội dung. Tìm và xem clip cần công cụ truy cập nguồn của môi trường AI; repo chưa tích hợp backend tải/transcribe tự động.

## Tải bộ tài liệu

```bash
git clone https://github.com/vilo0411/hook-script-kit.git
cd hook-script-kit
```

Không dùng Git: chọn **Code → Download ZIP** trên GitHub rồi giải nén.

## Codex — cài cho một project

Từ thư mục repo vừa tải, thay đường dẫn đích bằng project bạn muốn dùng:

```bash
HOOK_TARGET="/path/to/your-project/.agents/skills"
mkdir -p "$HOOK_TARGET"
if [ -e "$HOOK_TARGET/hook-script" ]; then
  echo "Đã có hook-script; hãy so sánh trước khi cập nhật."
else
  cp -R skills/hook-script "$HOOK_TARGET/hook-script"
fi
```

Mở một phiên Codex trong project đó. Yêu cầu:

```text
Dùng $hook-script tìm clip giáo dục tài chính phù hợp chủ đề lạm phát,
phân tích trước rồi đề xuất hook. Ghi rõ nguồn và phạm vi đã kiểm.
```

Muốn dùng cho mọi project, dùng cùng đoạn lệnh nhưng đặt `HOOK_TARGET="$HOME/.agents/skills"`. Vị trí project và cá nhân theo [tài liệu skills của OpenAI](https://developers.openai.com/codex/skills/).

## Claude Code — cài cho một project

Chạy lại đoạn sao chép ở trên với `HOOK_TARGET="/path/to/your-project/.claude/skills"`. Mở phiên Claude Code trong project rồi nhập:

```text
/hook-script Tìm và phân tích clip cùng chủ đề lạm phát rồi đề xuất hook có dẫn nguồn.
```

Muốn dùng cá nhân, đặt `HOOK_TARGET="$HOME/.claude/skills"`. Hướng dẫn này dành cho phiên chạy tại máy, theo [tài liệu Claude Code](https://code.claude.com/docs/en/skills).

## Công cụ chat khác

Không cần cài skill. Mở một trong [ba prompt](prompts/01-tao-hook.md), sao chép toàn bộ khối văn bản, điền đầu vào và gửi vào chat. Các prompt dùng độc lập. Nếu muốn thêm mẫu, đính kèm tài liệu Markdown liên quan; không giả định công cụ chat đọc được một đường dẫn trên máy bạn.

## Cập nhật hoặc gỡ

Chạy `git pull --ff-only` trong bản clone. So sánh thư mục skill mới với bản đã cài, giữ bản sao nếu bạn đã sửa riêng, rồi chủ động thay cả thư mục. Không ghép hai phiên bản chỉ bằng cách chép thêm file.

Gỡ bằng cách xóa đúng thư mục `hook-script` đã cài. Việc gỡ không xóa các kịch bản bạn đã viết.
