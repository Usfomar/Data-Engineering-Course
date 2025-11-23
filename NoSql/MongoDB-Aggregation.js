/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

use("training");

//the maximum grade scored of each subject
db.marks.aggregate([
	{
		$group: {
			_id: "$subject",
			Highest_Grade_Scored: { $max: "$marks" },
		},
	},
]);

//The minimum marks scored by each student

db.marks.aggregate([
	{
		$group: {
			_id: "$name",
			Minimum_Grade: { $min: "$marks" },
		},
	},
]);

//Top 2 subjects based on average marks
db.marks.aggregate([
	{
		$group: {
			_id: "$subject",
			Average_Marks: { $avg: "$marks" },
		},
	},
	{
		$sort: { Average_Marks: -1 },
	},
	{
		$limit: 2,
	},
]);
