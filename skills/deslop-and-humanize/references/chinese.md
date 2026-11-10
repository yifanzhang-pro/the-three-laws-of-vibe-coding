# Chinese prose

Read this with [patterns.md](patterns.md) when the text is Chinese. Everything there still applies; this file lists the forms the same problems take in Chinese and the cases to leave alone. The phrases are places to look, not a list of banned words.

## Translationese

Much machine-written Chinese is English syntax with Chinese words. Rewrite the sentence the way a Chinese writer would say it; swapping one word rarely helps.

| Cue | Example | Usually better | Leave alone when |
| --- | --- | --- | --- |
| 被 where Chinese needs no passive marker | 该方法被广泛应用于图像分类 | 该方法广泛用于图像分类 | The subject suffers the action (被攻击, 被拒稿), or the agent matters |
| 进行、加以、予以、作出 + a verb turned into a noun | 对数据进行了分析 | 分析了数据 | The object is long, or the genre is formal enough to expect it |
| 一个、一种 used as an English article | 作为一个研究者 | 作为研究者 | The count is the point: 一种方法 against 两种方法 |
| A long stack of 的 before the noun | 一个基于共享缓存的用于降低延迟的新的方法 | 新方法用共享缓存降低延迟 | The modifier is short, or it is a defined term |
| Framing phrases | 通过…的方式、在…方面、对于…而言、在…的过程中、在…的情况下 | Drop the frame and keep its content | The frame carries a condition: 在 batch size 为 8 的情况下 |
| 当…时、如果…的话 on every condition | 当用户点击按钮时，系统会… | 用户点击按钮后，系统… | The timing or the condition needs the emphasis |
| Abstract nouns in a row | 实现了流程的规范化、标准化、体系化 | Say what changed | Each noun names something measured: 可扩展性, 鲁棒性 |
| Pronouns English needs and Chinese drops | 它的性能、我们的方法的优点 | 性能、本方法的优点 | Dropping the pronoun makes the referent unclear |
| …之一 added by habit | 最重要的因素之一 | Keep or drop according to the facts | There really are several, and the text does not rank them |

## Empty official and marketing register

赋能、助力、抓手、闭环、打通、沉淀、全方位、多维度、深度融合、有效提升、充分彰显、具有重要意义、奠定坚实基础、提供有力支撑、日益凸显 often stand where a result should be. Ask what happened and write that. If the passage does not say, cut the phrase; do not supply a result.

Leave these words alone when they are technical terms (闭环控制, 多维度量表), when a measured result follows (有效提升 followed by the number can lose 有效 and keep the rest), and when the document is official writing in which the user wants the conventional register.

## Staged openings and closings

Openers that postpone the point: 值得注意的是、需要指出的是、众所周知、不可否认、随着…的快速发展、在当今…的时代、先说结论、划重点. Closers that repeat it: 综上所述、总而言之、总的来说、由此可见 followed by a restatement, 这才是真正的价值、希望本文对你有所帮助、让我们拭目以待.

Start at the content. Keep 综上 when a new conclusion does follow from the points above it, and keep 近年来 or a date when it limits the claim in time.

## Manufactured contrast and self-questioning

不是…而是…、不仅…更…、与其说…不如说…、这不只是…更是… deserve the test in patterns.md: does the rejected half tell the reader anything? The same holds for a question the writer asks only to answer it: 为什么？因为…、答案是肯定的、那么问题来了.

Keep the contrast that corrects a misunderstanding the reader is likely to have, and 不仅…而且… when both halves are facts.

## Scaffolding and parallelism

首先、其次、再次、最后 help when the points have an order or the reader has to count them. On three loosely related remarks they are scaffolding. 一方面…另一方面… needs two sides that pull against each other.

Three or four parallel phrases (高效、稳定、可靠; 看得见、摸得着、用得上) and runs of four-character phrases read as slogans. Keep the items that are true and distinct, and say them plainly. Do not drop a real list item to break the rhythm.

## Qualifiers

可能在一定程度上或许 is one qualifier written three times; keep one. 在一定程度上、一定的、某种意义上、相对而言 often mean nothing; cut them when the sentence makes the same claim without them. Real limits stay: 在本数据集上、初步结果表明、尚未验证、平均、至少、仅.

## Register

- Do not humanize by adding 说实话、其实吧、咱们、你敢信？ or internet slang. Spoken particles belong in text that is already conversational.
- Keep the author's choices of 您 or 你, 我们 or 笔者 or 本文, and Simplified or Traditional characters, along with the regional vocabulary (软件 and 軟體, 信息 and 資訊).
- An academic paper stays in written Chinese (书面语); a chat message or a post on a personal account may be loose. Match the document, not a general idea of natural language.

## Terms, punctuation, and spacing

- Keep the document's rendering of each term. Do not alternate 鲁棒性 and 稳健性, or translate a term the author left in English (batch size, token, Transformer). Leave personal and organization names as written.
- Use full-width punctuation in Chinese sentences and half-width inside English, code, and numbers. Keep 、 between parallel items. Follow the document on “” or 「」 and on spaces between Chinese and Latin characters; do not add or remove those spaces across a file.
- A string of —— or of bold phrases with colons (**优势：**…) is the same problem as its English counterpart. Fix the relationship between the clauses; do not just delete the mark.
- Numbers, units, and formulas are data: 120 ms, 18%, 3 次实验 stay exactly as written.

## Mixed-language documents

Edit each passage in its own language. Do not translate one into the other to make the document uniform unless asked. When the user writes to you in Chinese about an English document, the document stays in English and the report to the user is in Chinese.
