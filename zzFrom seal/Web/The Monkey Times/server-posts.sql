DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS posts ( id INTEGER PRIMARY KEY AUTOINCREMENT, title text, content text );
INSERT INTO posts ( title,content ) VALUES ( "Welcome!" ,"Welcome to Monkey's posts site!" );
INSERT INTO posts ( title,content ) VALUES ( "What are monkeys?", "Monkey is a common name that may refer to most mammals of the infraorder Simiiformes, also known as the simians. Traditionally, all animals in the group now known as simians are counted as monkeys except the apes, thus monkeys (in that sense) constitute an incomplete paraphyletic grouping; however, in the broader sense based on cladistics, apes (Hominoidea) are also included, making the terms monkeys and simians synonyms in regard to their scope." );
INSERT INTO posts ( title,content ) VALUES ( "Flag", "ApeCTF{sql1_1s_4_gr34t_vuln}" );
